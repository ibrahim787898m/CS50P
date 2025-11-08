from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("HELLO") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20

def test_other():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("123hello") == 100
