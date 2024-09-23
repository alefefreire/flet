from unittest.mock import MagicMock, patch

import flet as ft  # type: ignore
import pytest

from src.views.password_view import PasswordGeneratorUI


@pytest.fixture
def mock_page():
    return MagicMock(spec=ft.Page)


@pytest.fixture
def password_generator_ui(mock_page):
    with patch("src.core.password_service.PasswordService") as mock_service:
        ui = PasswordGeneratorUI(mock_page)
        ui.password_service = mock_service

        # Simulate the UI elements
        ui.generate_button = MagicMock()
        ui.generate_button.current = MagicMock()
        ui.txt_password = MagicMock()
        ui.btn_clipboard = MagicMock()
        ui.options = {}

        return ui


def test_init(password_generator_ui):
    assert isinstance(password_generator_ui.page, MagicMock)
    assert isinstance(password_generator_ui.password_service, MagicMock)


def test_toggle_option(password_generator_ui):
    mock_event = MagicMock()
    mock_event.control.data = "uppercase"
    mock_event.control.value = True

    password_generator_ui.toggle_option(mock_event)

    assert password_generator_ui.options == {"uppercase": True}
    assert password_generator_ui.generate_button.current.disabled is False
    assert password_generator_ui.generate_button.current.opacity == 1


def test_toggle_option_all_false(password_generator_ui):
    mock_event = MagicMock()
    mock_event.control.data = "uppercase"
    mock_event.control.value = False

    password_generator_ui.toggle_option(mock_event)

    assert password_generator_ui.options == {"uppercase": False}
    assert password_generator_ui.generate_button.current.disabled is True
    assert password_generator_ui.generate_button.current.opacity == 0.3


def test_generate_password_success(password_generator_ui):
    password_generator_ui.n_chars.current = MagicMock(value=10)
    password_generator_ui.options = {
        "uppercase": True,
        "lowercase": True,
        "numbers": True,
        "symbols": True,
    }
    mock_password = MagicMock(value="TestPassword123!")
    password_generator_ui.password_service.generate_password.return_value = (
        mock_password
    )

    password_generator_ui.generate_password(None)

    password_generator_ui.password_service.generate_password.assert_called_once_with(
        length=10,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )
    assert password_generator_ui.txt_password.current.value == "TestPassword123!"


def test_generate_password_error(password_generator_ui):
    password_generator_ui.n_chars.current = MagicMock(value=10)
    password_generator_ui.options = {}
    password_generator_ui.password_service.generate_password.side_effect = ValueError(
        "Error message"
    )

    password_generator_ui.generate_password(None)

    assert password_generator_ui.txt_password.current.value == "Error message"


def test_copy_to_clipboard(password_generator_ui):
    password_generator_ui.txt_password.current = MagicMock(value="TestPassword123!")

    password_generator_ui.copy_to_clipboard(None)

    password_generator_ui.page.set_clipboard.assert_called_once_with("TestPassword123!")
    assert password_generator_ui.btn_clipboard.current.selected is True
