from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("h") == 20


def test_others():
    assert value("Whats'up") == 100


def test_uppercase():
    assert value("HELLO") == 0


def test_string():
    assert value("hello taran") == 0