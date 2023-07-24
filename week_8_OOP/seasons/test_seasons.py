import pytest
from seasons import get_dob, difference


def test_invalid_date():
    with pytest.raises(SystemExit):
        get_dob("2022-13-32")
        get_dob("20222-123-234")
