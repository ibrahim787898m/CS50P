import os
import sys
import csv
import re
import signal
from pathlib import Path
from datetime import datetime
from tabulate import tabulate
from fpdf import FPDF
from fpdf.enums import XPos, YPos

def main():
    signal.signal(signal.SIGINT, handle_stop)
    signal.signal(signal.SIGTSTP, handle_stop)

    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py <filename.csv>")

    filename = Path(sys.argv[1])

    if filename.suffix.lower() != ".csv":
        sys.exit("Error: File must have a .csv extension")

    if not filename.exists():
        print(f"File '{filename}' not found. Creating a new one...")
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Date", "Category", "Amount", "Note"])
            writer.writeheader()

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
            date = get_valid_date()
            category = get_valid_category()
            amount = get_valid_amount()
            note = get_valid_note()
            add_expense(filename, date, category, amount, note)
            print("Expense added successfully!")
        elif choice == "2":
            view_expense(filename)
        elif choice == "3":
            export(filename)
        elif choice == "4":
            delete_expense(filename)
        elif choice == "5":
            dash()
            print("👋 Goodbye! Thanks for using Expense Tracker.")
            dash()
            break
        else:
            print("Invalid choice!")

def handle_stop(signum, frame):
    print("\n👋 Program stopped safely. Goodbye!")
    dash()
    sys.exit(0)

def dash():
    print("-" * 70)

def get_valid_date():
    while True:
        date = input("Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

def get_valid_category():
    while True:
        category = input("Category: ")
        if re.fullmatch(r"[A-Za-z\s\-]+", category):
            return category
        else:
            print("Invalid category! Only letters, spaces and dashes are allowed.")

def get_valid_amount():
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

def get_valid_note():
    return input("Note: ")

def add_expense(flnm, dt, ctgry, amnt, nt):
    fieldnames = ["Date", "Category", "Amount", "Note"]
    with open(flnm, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({
            "Date": dt,
            "Category": ctgry,
            "Amount": amnt,
            "Note": nt
        })

def view_expense(flnm):
    with open(flnm, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    if len(data) <= 1:
        print("No expenses recorded yet!")
        return

    print(tabulate(data, headers="firstrow", tablefmt="grid"))

def export(flnm):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)

    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "Expense Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(40, 10, "Date", border=1)
    pdf.cell(40, 10, "Category", border=1)
    pdf.cell(40, 10, "Amount", border=1)
    pdf.cell(70, 10, "Note", border=1)
    pdf.ln()

    pdf.set_font("helvetica", size=12)

    with open(flnm, "r") as csvfile:
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

    name, ext = os.path.splitext(flnm)
    pdf.output(f"{name}.pdf")
    print(f"Exported as {name}.pdf")

def view_expense_with_index(flnm):
    """Display expenses with row numbers for deletion"""
    with open(flnm, "r") as csvfile:
        reader = list(csv.reader(csvfile))
        if len(reader) <= 1:
            print("No expenses recorded yet!")
            return []

    print("Index | Date | Category | Amount | Note")
    for idx, row in enumerate(reader[1:], start=1):
        date, category, amount, note = row
        print(f"{idx} | {date} | {category} | {amount} | {note}")

    return reader

def delete_expense(flnm):
    reader = view_expense_with_index(flnm)
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

    with open(flnm, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(reader)

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\n👋 Program stopped safely. Goodbye!")
        dash()
