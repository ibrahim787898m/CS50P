"""
project.py

Expense Tracker (CS50P Final Project)

A command-line expense tracker application built with Python. This program allows users to:

- Login with credentials stored in a JSON file
- Add, view, and delete expenses
- Export expenses to a PDF report
- Validate user inputs (date, category, amount, note)
- Handle program interruptions safely (Ctrl+C / EOF)
- Demonstrate object-oriented programming (OOP) design

Dependencies:
- tabulate >= 0.9.0
- fpdf >= 2.5.5
"""

import os
import sys
import csv
import re
import json
import signal
from pathlib import Path
from datetime import datetime
from tabulate import tabulate
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class Expense:
    """
    Represents a single expense entry.

    Attributes:
        date (str): Date of the expense in YYYY-MM-DD format.
        category (str): Category of the expense (e.g., Food, Transport).
        amount (float): Amount spent.
        note (str): Optional note describing the expense.
    """

    def __init__(self, date, category, amount, note):
        """Initialize a new expense with date, category, amount, and note."""
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_list(self):
        """
        Convert the expense to a list for CSV writing.

        Returns:
            list[str]: [date, category, str(amount), note]
        """
        return [self.date, self.category, str(self.amount), self.note]

class ExpenseTracker:
    """
    Handles the core functionality of tracking expenses.

    Methods:
        add_expense(expense): Adds a new Expense to the CSV file.
        view_expense(): Displays all expenses in a table format.
        delete_expense(): Deletes an expense by index.
        export_pdf(): Exports all expenses to a PDF report.
    """

    FIELDNAMES = ["Date", "Category", "Amount", "Note"]

    def __init__(self, filename):
        """Initialize tracker with a CSV filename and create file if it does not exist."""
        self.filename = Path(filename)
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        """Create CSV file with headers if it does not exist."""
        if not self.filename.exists():
            print(f"File '{self.filename}' not found. Creating a new one...")
            with open(self.filename, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
                writer.writeheader()

    def add_expense(self, expense: Expense):
        """
        Add a new expense entry to the CSV file.

        Args:
            expense (Expense): Expense object to be added.
        """
        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
            writer.writerow({
                "Date" : expense.date,
                "Category" : expense.category,
                "Amount" : expense.amount,
                "Note" : expense.note
            })
        print("Expense added succesfully!")

    def view_expense(self):
        """
        Display all expenses in a table format using tabulate.
        Prints a message if no expenses exist.
        """
        with open(self.filename, "r") as csvfile:
            reader = list(csv.reader(csvfile))
            if len(reader) <= 1:
                print("No expenses recorded yet!")
                return
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    def export_pdf(self):
        """
        Export all expenses as a PDF using FPDF.
        Also calculate the total expense at the end.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)

        # Title
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 10, "Expense Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        pdf.ln(5)

        # Table headers
        pdf.set_font("helvetica", "B", 12)
        pdf.cell(40, 10, "Date", border=1)
        pdf.cell(40, 10, "Category", border=1)
        pdf.cell(40, 10, "Amount", border=1)
        pdf.cell(70, 10, "Note", border=1)
        pdf.ln()

        pdf.set_font("helvetica", size=12)
        with open(self.filename, "r") as csvfile:
            reader = list(csv.reader(csvfile))

        if len(reader) <= 1:
            print("No expenses to export yet!")
            return

        total_amount = 0
        for row in reader[1:]:
            date, category, amount, note = row
            total_amount += float(amount)
            pdf.cell(40, 10, date, border=1)
            pdf.cell(40, 10, category, border=1)
            pdf.cell(40, 10, f"${amount}", border=1)
            pdf.cell(70, 10, note, border=1)
            pdf.ln()

        pdf.set_font("helvetica", "B", 12)
        pdf.cell(80, 10, "Total", border=1)
        pdf.cell(110, 10, f"${total_amount:.2f}", border=1, align="C")
        pdf.ln()

        name, _ = os.path.splitext(self.filename)
        pdf.output(f"{name}.pdf")
        print(f"Exported as {name}.pdf")

    def view_expenses_with_index(self):
        """
        Display all the expenses with the index number.
        This one is for deleting expenses according to the index number.
        """
        with open(self.filename, "r") as csvfile:
            reader = list(csv.reader(csvfile))
            if len(reader) <= 1:
                print("No expenses recorded yet!")
                return []

        print("Index | Date | Category | Amount | Note")
        for idx, row in enumerate(reader[1:], start=1):
            date, category, amount, note = row
            print(f"{idx} | {date} | {category} | {amount} | {note}")

        return reader

    def delete_expense(self):
        """
        This will delete the expense according to the index number inputed.
        """
        reader = self.view_expenses_with_index()
        if not reader or len(reader) <= 1:
            return

        while True:
            try:
                idx = int(input("Enter the index of the expense to delete: "))
                if 1 <= idx < len(reader):
                    break
                else:
                    print(f"Invalid index! Enter a number between 1 and {len(reader)-1}")
            except ValueError:
                print("Invalid input! Enter a number.")

        deleted_row = reader.pop(idx)
        print(f"Deleted expense: {deleted_row}")

        with open(self.filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(reader)

class UserValidator:
    """
    Handles user authentication and configuration loading.

    Methods:
        load_config(cnfg_fl): Load user credentials from JSON.
        login(cnfg_fl): Authenticate user with username/password.
    """

    @staticmethod
    def load_config(cnfg_fl):
        """
        Load the JSON configuration file containing user credentials.

        Args:
            cnfg_fl (str): Path to configuration JSON file.

        Returns:
            dict: Configuration data containing users.
        """
        if not os.path.exists(cnfg_fl):
            default_config = {"users": {"ibrahimM": "787898"}}
            with open(cnfg_fl, "w") as f:
                json.dump(default_config, f, indent=4)
        with open(cnfg_fl, "r") as f:
            return json.load(f)

    @staticmethod
    def login(cnfg_fl):
        """
        Authenticate user using credentials stored in JSON.

        Args:
            cnfg_fl (str): Path to configuration JSON file.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        config = UserValidator.load_config(cnfg_fl)
        users = config.get("users", {})
        for uname in users:
            username = uname
        dash()
        print(f"👋 Welcome, {username}, to your expense tracker!")
        print("Enter your username and password to log in!")
        dash()
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            dash()
            print("✅ Login successful!")
            dash()
            return True
        else:
            dash()
            print("❌ Invalid credentials.")
            return False

class InputValidator:
    """
    Handles validation of user inputs for the expense tracker.

    Methods:
        get_valid_date(): Prompt user until a valid YYYY-MM-DD date is entered.
        get_valid_category(): Prompt user until a valid category is entered.
        get_valid_amount(): Prompt user until a positive number is entered.
        get_valid_note(): Prompt user for a note (no validation).
    """

    @staticmethod
    def get_valid_date():
        """Return a validated date string (YYYY-MM-DD) entered by the user."""
        while True:
            date = input("Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return date
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")

    @staticmethod
    def get_valid_category():
        """Return a validated category string entered by the user."""
        while True:
            category = input("Category: ")
            if re.fullmatch(r"[A-Za-z\s\-]+", category):
                return category
            else:
                print("Invalid category! Only letters, spaces and dashes are allowed.")

    @staticmethod
    def get_valid_amount():
        """Return a validated positive float amount entered by the user."""
        while True:
            amount = input("Amount: ")
            try:
                amount = float(amount)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be greater than zero!")
            except ValueError:
                print("Invalid input! Please enter a number.")

    @staticmethod
    def get_valid_note():
        """Prompt the user for a note and return it (no validation)."""
        return input("Note: ")

# --------------------------
# Top-level wrapper functions
# --------------------------
def add_expense_ui(tracker):
    """Wrapper function to get user input and add an expense."""
    date = InputValidator.get_valid_date()
    category = InputValidator.get_valid_category()
    amount = InputValidator.get_valid_amount()
    note = InputValidator.get_valid_note()
    expense = Expense(date, category, amount, note)
    tracker.add_expense(expense)


def view_expenses_ui(tracker):
    """Wrapper function to view all expenses."""
    tracker.view_expense()


def export_expenses_ui(tracker):
    """Wrapper function to export expenses to PDF."""
    tracker.export_pdf()

# --------------------------
# Main program functions
# --------------------------
def main():
    """
    Main program loop.

    - Handles user login
    - Initializes ExpenseTracker
    - Displays menu for add/view/delete/export/quit
    - Uses top-level wrapper functions to interact with tracker
    """
    signal.signal(signal.SIGINT, handle_stop)
    signal.signal(signal.SIGTSTP, handle_stop)

    config_file = "config.json"
    if not UserValidator.login(config_file):
        print("Exiting due to invalid login...")
        dash()
        sys.exit()

    while True:
        filename = input("File Name: ")

        if not filename.lower().endswith(".csv"):
            print("Error: File must have a .csv extension")
            continue
        else:
            break

    tracker = ExpenseTracker(filename)

    while True:
        dash()
        print("Expense Tracker")
        dash()
        print("1. Add expense")
        print("2. View expense")
        print("3. Export")
        print("4. Delete expense")
        print("5. Quit")
        dash()

        choice = input("Choose: ")

        if choice == "1":
            add_expense_ui(tracker)
        elif choice == "2":
            view_expenses_ui(tracker)
        elif choice == "3":
            export_expenses_ui(tracker)
        elif choice == "4":
            tracker.delete_expense()
        elif choice == "5":
            dash()
            print("👋 Goodbye! Thanks for using the Expense Tracker.")
            dash()
            break
        else:
            print("Invalid choice!")


def dash():
    """Print a horizontal divider line."""
    print("-" * 70)

def handle_stop(signum, frame):
    """Handle Ctrl+C or Ctrl+Z safely by exiting the program."""
    print("\n👋 Program stopped safely. Goodbye!")
    dash()
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\n👋 Program stopped safely. Goodbye!")
        dash()
