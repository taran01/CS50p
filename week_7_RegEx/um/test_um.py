from um import count


def test_once():
    assert count("um") == 1


def test_word():
    assert count("Bump lump") == 0


def test_followedby():
    assert count("um, um? $um?") == 3


def test_string():
    assert count("Um, thanks for the album.") == 1


def test_casein():
    assert count("Um, thanks, um...") == 2