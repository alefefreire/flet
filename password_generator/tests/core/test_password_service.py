import pytest

from src.core.password_service import PasswordService
from src.domain.models import Password


@pytest.fixture
def password_service():
    return PasswordService()


def test_generate_password_all_types(password_service):
    password = password_service.generate_password(12, True, True, True, True)
    assert isinstance(password, Password)
    assert len(password.value) == 12


def test_generate_password_uppercase_only(password_service):
    password = password_service.generate_password(8, True, False, False, False)
    assert isinstance(password, Password)
    assert len(password.value) == 8
    assert password.value.isupper()


def test_generate_password_lowercase_only(password_service):
    password = password_service.generate_password(10, False, True, False, False)
    assert isinstance(password, Password)
    assert len(password.value) == 10
    assert password.value.islower()


def test_generate_password_numbers_only(password_service):
    password = password_service.generate_password(6, False, False, True, False)
    assert isinstance(password, Password)
    assert len(password.value) == 6
    assert password.value.isdigit()


def test_generate_password_symbols_only(password_service):
    password = password_service.generate_password(7, False, False, False, True)
    assert isinstance(password, Password)
    assert len(password.value) == 7
    assert all(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for char in password.value)


def test_generate_password_specific_length(password_service):
    length = 15
    password = password_service.generate_password(length, True, True, True, True)
    assert isinstance(password, Password)
    assert len(password.value) == length
