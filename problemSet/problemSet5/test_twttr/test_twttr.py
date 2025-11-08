from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_mixedcase():
    assert shorten("CS50p") == "CS50p"  # no vowels removed except 'o'
    assert shorten("Python") == "Pythn"

def test_numbers():
    assert shorten("CS50") == "CS50"  # numbers should stay unchanged

def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"
