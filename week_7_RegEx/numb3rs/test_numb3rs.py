from numb3rs import validate


def test_strings():
    assert validate("cat") == False


def test_outofrange():
    assert validate("125.125.125.125.125") == False


def test_lessvalues():
    assert validate("175.512.512.512") == False


