from datetime import date
from seasons import calculate_minutes  # replace 'seasons' with your filename

def test_calculate_minutes_basic():
    # Example: birthdate = Jan 1, 2000
    b_date = date(2000, 1, 1)
    today = date.today()
    expected_minutes = (today - b_date).days * 24 * 60
    assert calculate_minutes(b_date) == expected_minutes

def test_calculate_minutes_today():
    # Birthdate is today → 0 minutes
    b_date = date.today()
    assert calculate_minutes(b_date) == 0

def test_calculate_minutes_yesterday():
    # Birthdate was yesterday → 1440 minutes
    b_date = date.today().replace(day=date.today().day - 1)
    assert calculate_minutes(b_date) == 1440
