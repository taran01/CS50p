import pytest
from fuel import convert, gauge


def test_full():
    assert convert("1/1") == 100


def test_empty():
    assert convert("0/1") == 0


def test_gauge_f():
    assert gauge(99) == "F"


def test_gauge_e():
    assert gauge(1) == "E"


def test_gauge_percentage():
    assert gauge(25) == "25%"


def test_zero_divisoin():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("10/5")