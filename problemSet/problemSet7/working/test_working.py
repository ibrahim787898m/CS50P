import pytest
from working import convert

def test_valid_hours():
    # Without minutes
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_with_minutes():
    # With minutes
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("1:05 AM to 1:05 PM") == "01:05 to 13:05"

def test_invalid():
    # Bad formats
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")  # hour > 12

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")  # minute > 59

    with pytest.raises(ValueError):
        convert("9AM - 5PM")  # wrong separator

    with pytest.raises(ValueError):
        convert("hello world")  # nonsense input
