import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_convert_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")   # denominator zero
    with pytest.raises(ValueError):
        convert("cat/dog")   # not numbers
    with pytest.raises(ValueError):
        convert("5/3")   # greater than 1
    with pytest.raises(ValueError):
        convert("-5/3")
