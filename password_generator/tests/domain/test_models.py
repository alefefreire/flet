import pytest
from pydantic import ValidationError

from src.domain.models import Password


def test_valid_password():
    password = Password(value="validpassword")
    assert password.value == "validpassword"


def test_empty_password():
    with pytest.raises(ValidationError):
        Password(value="")


def test_whitespace_password():
    with pytest.raises(ValidationError):
        Password(value="   ")
