import flet as ft

def login(page, criar_conta, esqueci_senha, sexta_feira):
    username_input = ft.TextField(label="Nome de Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    error_message = ft.Text("", color=ft.colors.RED)

    def verificar_login(e):

        error_message.value = ""

        if not username_input.value or not password_input.value:
            error_message.value = 'Por favor preencha todos os campos!'
            page.update()
            return


        page.controls.clear()
        sexta_feira(page)

    # Adiciona os controles da página de login
    page.controls.clear()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Login", size=30),
                username_input,
                password_input,
                error_message,
                ft.ElevatedButton(text="Login", width=300, on_click=verificar_login),
                ft.TextButton(text="Esqueci a senha", width=300, on_click=lambda e: esqueci_senha(page)),
                ft.TextButton(text="Criar conta", width=300, on_click=lambda e: criar_conta(page)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )
    
    page.update()
