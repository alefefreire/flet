import string

import pytest

from src.domain.password_generator import PasswordGenerator


@pytest.fixture
def generator():
    return PasswordGenerator()


def test_generate_password_with_all_characters(generator):
    password = generator.generate(12, True, True, True, True)
    assert len(password.value) == 12
    assert any(c.isupper() for c in password.value)
    assert any(c.islower() for c in password.value)
    assert any(c.isdigit() for c in password.value)
    assert any(c in string.punctuation for c in password.value)


def test_generate_password_with_uppercase_only(generator):
    password = generator.generate(8, True, False, False, False)
    assert len(password.value) == 8
    assert all(c.isupper() for c in password.value)


def test_generate_password_with_lowercase_only(generator):
    password = generator.generate(10, False, True, False, False)
    assert len(password.value) == 10
    assert all(c.islower() for c in password.value)


def test_generate_password_with_numbers_only(generator):
    password = generator.generate(6, False, False, True, False)
    assert len(password.value) == 6
    assert all(c.isdigit() for c in password.value)


def test_generate_password_with_symbols_only(generator):
    password = generator.generate(7, False, False, False, True)
    assert len(password.value) == 7
    assert all(c in string.punctuation for c in password.value)


def test_generate_password_with_no_characters_selected(generator):
    with pytest.raises(ValueError):
        generator.generate(5, False, False, False, False)
