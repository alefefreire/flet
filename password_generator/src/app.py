import flet as ft  # type: ignore

from src.views.password_view import PasswordGeneratorUI


def main(page: ft.Page):
    PasswordGeneratorUI(page)


if __name__ == "__main__":
    ft.app(target=main)
