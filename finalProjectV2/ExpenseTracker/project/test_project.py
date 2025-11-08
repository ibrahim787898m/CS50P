import os
import csv
import json
import pytest
from pathlib import Path
from project import Expense, ExpenseTracker, InputValidator, UserValidator

TEST_FILE = "test_expenses.csv"
TEST_CONFIG = "test_config.json"

# --------------------------
# Setup / Teardown
# --------------------------
def setup_module(module):
    """Remove test files before running tests."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(TEST_CONFIG):
        os.remove(TEST_CONFIG)
    # Create a test config file with one user
    test_data = {"users": {"testuser": "testpass"}}
    with open(TEST_CONFIG, "w") as f:
        json.dump(test_data, f, indent=4)

def teardown_module(module):
    """Clean up test files after tests."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(TEST_CONFIG):
        os.remove(TEST_CONFIG)
    pdf_file = f"{os.path.splitext(TEST_FILE)[0]}.pdf"
    if os.path.exists(pdf_file):
        os.remove(pdf_file)

# --------------------------
# Expense Class Tests
# --------------------------
def test_expense_to_list():
    expense = Expense("2025-11-06", "Food", 15.5, "Lunch")
    assert expense.to_list() == ["2025-11-06", "Food", "15.5", "Lunch"]

# --------------------------
# ExpenseTracker Tests
# --------------------------
def test_add_and_view_expense():
    tracker = ExpenseTracker(TEST_FILE)
    expense = Expense("2025-11-06", "Transport", 10, "Bus fare")
    tracker.add_expense(expense)

    with open(TEST_FILE, "r") as f:
        reader = list(csv.reader(f))

    assert len(reader) == 2  # header + one expense
    assert reader[1] == ["2025-11-06", "Transport", "10", "Bus fare"]

def test_delete_expense_logic():
    # Ensure CSV is fresh
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    tracker = ExpenseTracker(TEST_FILE)
    # Add 2 expenses
    tracker.add_expense(Expense("2025-11-06", "Food", 20, "Dinner"))
    tracker.add_expense(Expense("2025-11-06", "Books", 30, "Python Book"))

    # Delete first expense manually
    rows = list(csv.reader(open(TEST_FILE)))
    rows.pop(1)  # remove first expense
    with open(TEST_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # Read back and check
    with open(TEST_FILE, "r") as f:
        reader = list(csv.reader(f))
    assert len(reader) == 2  # header + remaining
    assert reader[1][1] == "Books"


def test_export_pdf_creates_file():
    tracker = ExpenseTracker(TEST_FILE)
    tracker.add_expense(Expense("2025-11-06", "Misc", 5, "Snack"))
    tracker.filename = TEST_FILE
    tracker.export_pdf()
    pdf_file = f"{os.path.splitext(TEST_FILE)[0]}.pdf"
    assert os.path.exists(pdf_file)
    os.remove(pdf_file)

# --------------------------
# InputValidator Tests
# --------------------------
def test_get_valid_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2025-11-06")
    date = InputValidator.get_valid_date()
    assert date == "2025-11-06"

def test_get_valid_amount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "25.5")
    amount = InputValidator.get_valid_amount()
    assert amount == 25.5

def test_get_valid_category(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Groceries")
    category = InputValidator.get_valid_category()
    assert category == "Groceries"

# --------------------------
# UserValidator / Login Tests
# --------------------------
def test_login_success(monkeypatch):
    inputs = iter(["testuser", "testpass"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = UserValidator.login(TEST_CONFIG)
    assert result == True

def test_login_failure(monkeypatch):
    inputs = iter(["wronguser", "wrongpass"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = UserValidator.login(TEST_CONFIG)
    assert result == False
