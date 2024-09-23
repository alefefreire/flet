from unittest.mock import MagicMock, patch

import flet as ft  # type: ignore
import pytest

from src.app import main


@pytest.fixture
def mock_page():
    return MagicMock(spec=ft.Page)


@pytest.fixture
def mock_password_generator_ui():
    with patch("src.app.PasswordGeneratorUI") as mock_ui:
        yield mock_ui


def test_main(mock_page, mock_password_generator_ui):
    main(mock_page)
    mock_password_generator_ui.assert_called_once_with(mock_page)
