import random
import string

import flet as ft


def main(page: ft.Page):
    # Refs
    options = {}
    generate_button = ft.Ref[ft.Container]()
    txt_password = ft.Ref[ft.Text]()
    n_chars = ft.Ref[ft.Slider]()
    btn_clipboard = ft.Ref[ft.IconButton]()

    # Functions
    def copy_to_clipboard(e):
        pwd = txt_password.current.value
        if pwd:
            page.set_clipboard(pwd)
            btn_clipboard.current.selected = True
            btn_clipboard.current.update()

    def toggle_option(e):
        nonlocal options
        options.update({e.control.data: e.control.value})
        if any(options.values()):
            generate_button.current.disabled = False
            generate_button.current.opacity = 1
        else:
            generate_button.current.disabled = True
            generate_button.current.opacity = 0.3

        generate_button.current.update()

    def generate_password(e):
        pwd = ""
        if options.get("uppercase"):
            pwd += string.ascii_uppercase
        if options.get("lowercase"):
            pwd += string.ascii_lowercase
        if options.get("numbers"):
            pwd += string.digits
        if options.get("symbols"):
            pwd += string.punctuation

        count = int(n_chars.current.value)
        password = "".join(random.choices(pwd, k=count))
        txt_password.current.value = password
        txt_password.current.update()

    # Page Configs
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#192233", on_primary="#ffffff", background="#0d121c"
        )
    )
    # Layout
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
                                ref=txt_password,
                                selectable=True,
                                size=20,
                                height=40,
                            ),
                            ft.IconButton(
                                ref=btn_clipboard,
                                icon=ft.icons.COPY,
                                icon_color=ft.colors.WHITE30,
                                selected_icon=ft.icons.CHECK,
                                selected_icon_color=ft.colors.INDIGO,
                                selected=False,
                                on_click=copy_to_clipboard,
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
                        ref=n_chars,
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
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(value="Include Lowercase", size=20),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.INDIGO,
                        data="lowercase",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(value="Include Numbers", size=20),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.INDIGO,
                        data="numbers",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(value="Include Symbols", size=20),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.INDIGO,
                        data="symbols",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.Container(
                    ref=generate_button,
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
                    on_click=generate_password,
                    disabled=True,
                    opacity=0.3,
                    animate_opacity=ft.Animation(
                        duration=700, curve=ft.AnimationCurve.DECELERATE
                    ),
                ),
            ],
        ),
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
