from plates import is_valid


def test_2letters():
    assert is_valid("12") == False


def test_minlen():
    assert is_valid("f") == False


def test_maxlen():
    assert is_valid("asd1234") == False


def test_punctuation():
    assert is_valid("as12-4") == False


def test_zero():
    assert is_valid("cs05") == False


def test_num_placement():
    assert is_valid("cs12p3") == False