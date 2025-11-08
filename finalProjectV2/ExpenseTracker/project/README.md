# Expense Tracker (CS50P Final Project)

A command-line expense tracker built in Python that helps users record, view, delete, and export their expenses. This project demonstrates object-oriented programming (OOP), file handling, input validation, and basic user authentication.

---

## **Features**

- Object-oriented design for expense management.
- Top-level wrapper functions to meet CS50P function requirements.
- User login system with credentials stored in `config.json`.
- Add expenses with date, category, amount, and note.
- View all recorded expenses in a table format.
- Delete expenses by index.
- Export expenses to a PDF report.
- Input validation for date, category, and amount.
- Handles program interruption gracefully (Ctrl+C / EOF).

---

## **Installation**

1. Clone this repository or download the files.
2. Make sure Python 3 is installed on your system.
3. Install required libraries:

```bash
pip install -r requirements.txt
```

---

## **Usage**

Run the program:

```bash
python project.py
```

**Login Credentials:**
- Default username: ibrahimM
- Default password: 787898

Once logged in, follow the menu to manage your expenses.

---

## **Project Structure**

```
project.py        # Main Python script
config.json       # User login credentials (auto-created if missing)
README.md         # Project description and instructions
requirements.txt  # Project dependencies
test_project.py   # Pytest file for main project.py file
```

---

## **Dependencies**

- tabulate>=0.9.0 – for displaying expenses in a table format
- fpdf>=2.5.5 – for exporting expenses to PDF

---

## 🎬 Demo Video
Watch the project demonstration here:
[▶️ Expense Tracker Demo (YouTube)](https://youtu.be/eoQ3vA9TLCk?si=tBQLj6Q2AlpsWeAo)
