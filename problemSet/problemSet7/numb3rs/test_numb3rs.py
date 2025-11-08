from numb3rs import validate

def test_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_false():
    assert validate("512-512-512-512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False

