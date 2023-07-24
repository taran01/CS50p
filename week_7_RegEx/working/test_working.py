import pytest
from working import convert


def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_outofrange():
    with pytest.raises(ValueError):
        convert("13 AM to 15 PM")
