from plates import is_valid

def test_one():
    assert is_valid("CS50") == True

def test_two():
    assert is_valid("CS05") == False

def test_three():
    assert is_valid("CS50P") == False

def test_four():
    assert is_valid("PI3.14") == False

def test_five():
    assert is_valid("H") == False

def test_six():
    assert is_valid("OUTATIME") == False
