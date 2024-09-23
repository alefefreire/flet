import flet as ft  # type: ignore

from src.core.password_service import PasswordService


class PasswordGeneratorUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.password_service = PasswordService()
        self.setup_view()

    def setup_view(self):
        # Refs
        self.options = {}
        self.generate_button = ft.Ref[ft.Container]()
        self.txt_password = ft.Ref[ft.Text]()
        self.n_chars = ft.Ref[ft.Slider]()
        self.btn_clipboard = ft.Ref[ft.IconButton]()

        # Page Configs
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#192233", on_primary="#ffffff", background="#0d121c"
            )
        )

        # Layout
        layout = self.create_layout()
        self.page.add(layout)

    def copy_to_clipboard(self, e: ft.event) -> None:
        pwd = self.txt_password.current.value
        if pwd:
            self.page.set_clipboard(pwd)
            self.btn_clipboard.current.selected = True
            self.btn_clipboard.current.update()

    def toggle_option(self, e: ft.event) -> None:
        self.options.update({e.control.data: e.control.value})
        if any(self.options.values()):
            self.generate_button.current.disabled = False
            self.generate_button.current.opacity = 1
        else:
            self.generate_button.current.disabled = True
            self.generate_button.current.opacity = 0.3

        self.generate_button.current.update()

    def generate_password(self, e: ft.event) -> None:
        try:
            password = self.password_service.generate_password(
                length=int(self.n_chars.current.value),
                use_uppercase=self.options.get("uppercase", False),
                use_lowercase=self.options.get("lowercase", False),
                use_numbers=self.options.get("numbers", False),
                use_symbols=self.options.get("symbols", False),
            )
            self.txt_password.current.value = password.value
            self.txt_password.current.update()
        except ValueError as err:
            self.txt_password.current.value = str(err)
            self.txt_password.current.update()

    def create_layout(self) -> ft.Container:
        layout = ft.Container(
            expand=True,
            padding=ft.padding.only(top=40, left=20, right=20, bottom=20),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[ft.colors.PRIMARY, ft.colors.BACKGROUND],
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Text(
                        value="Password Generator",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Divider(height=30, thickness=0.5),
                    ft.Container(
                        bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                        border_radius=ft.border_radius.all(5),
                        padding=ft.padding.all(10),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    ref=self.txt_password,
                                    selectable=True,
                                    size=20,
                                    height=40,
                                ),
                                ft.IconButton(
                                    ref=self.btn_clipboard,
                                    icon=ft.icons.COPY,
                                    icon_color=ft.colors.WHITE30,
                                    selected_icon=ft.icons.CHECK,
                                    selected_icon_color=ft.colors.INDIGO,
                                    selected=False,
                                    on_click=self.copy_to_clipboard,
                                ),
                            ],
                        ),
                    ),
                    ft.Text(
                        value="number of characters".upper(),
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(
                        bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                        border_radius=ft.border_radius.all(5),
                        padding=ft.padding.all(10),
                        content=ft.Slider(
                            ref=self.n_chars,
                            min=4,
                            max=20,
                            value=10,
                            divisions=10,
                            label="{value}",
                        ),
                    ),
                    ft.Text(
                        value="preferences".upper(),
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.ListTile(
                        title=ft.Text(value="Include Uppercase", size=20),
                        trailing=ft.Switch(
                            adaptive=True,
                            active_color=ft.colors.INDIGO,
                            data="uppercase",
                            on_change=self.toggle_option,
                        ),
                        toggle_inputs=True,
                    ),
                    ft.ListTile(
                        title=ft.Text(value="Include Lowercase", size=20),
                        trailing=ft.Switch(
                            adaptive=True,
                            active_color=ft.colors.INDIGO,
                            data="lowercase",
                            on_change=self.toggle_option,
                        ),
                        toggle_inputs=True,
                    ),
                    ft.ListTile(
                        title=ft.Text(value="Include Numbers", size=20),
                        trailing=ft.Switch(
                            adaptive=True,
                            active_color=ft.colors.INDIGO,
                            data="numbers",
                            on_change=self.toggle_option,
                        ),
                        toggle_inputs=True,
                    ),
                    ft.ListTile(
                        title=ft.Text(value="Include Symbols", size=20),
                        trailing=ft.Switch(
                            adaptive=True,
                            active_color=ft.colors.INDIGO,
                            data="symbols",
                            on_change=self.toggle_option,
                        ),
                        toggle_inputs=True,
                    ),
                    ft.Container(
                        ref=self.generate_button,
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(20),
                        border_radius=ft.border_radius.all(5),
                        gradient=ft.LinearGradient(
                            colors=[ft.colors.INDIGO_900, ft.colors.INDIGO_600],
                        ),
                        content=ft.Text(
                            value="Generate Password",
                            weight=ft.FontWeight.BOLD,
                        ),
                        on_click=self.generate_password,
                        disabled=True,
                        opacity=0.3,
                        animate_opacity=ft.Animation(
                            duration=700, curve=ft.AnimationCurve.DECELERATE
                        ),
                    ),
                ],
            ),
        )
        return layout
