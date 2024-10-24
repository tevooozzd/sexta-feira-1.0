import flet as ft

def main(page: ft.Page):
    page.title = "Página de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900

    def confirmar_login(e):
        if not username_input.value:
            username_input.error_text = "Por favor digite um usuário!"
            page.update()
        if not password_input.value:
            password_input.error_text = "Por favor digite uma senha!"
            page.update()

        else:
            username = username_input.value
            password = password_input.value

            page.clean()
            bem_vindo = ft.Text(f"Seja bem-vindo {username}! Esse é a primeira versão (1.0) da inteligencia artificial 'SEXTA-FERIA' ")
            page.add(bem_vindo)

    username_input = ft.TextField(
        label="Nome de Usuário",
        width=300,
        bgcolor=ft.colors.WHITE,
    )

    password_input = ft.TextField(
        label="Senha",
        password=True,
        width=300,
        bgcolor=ft.colors.WHITE,
    )

    confirmar_login_button = ft.ElevatedButton(
        text="Login",
        on_click=confirmar_login,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_600,
        width=300,
    )

    page.add(
        ft.Column(
            controls=[
                username_input,
                password_input,
                confirmar_login_button
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Executando o app
ft.app(target=main)
