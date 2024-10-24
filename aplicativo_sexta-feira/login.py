import flet as ft

def main(page: ft.Page):
    # Design dá pagina principal
    page.title = "SEXTA-FEIRA 1.0"
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Variavéis para guardar login e senha
    username_input = ft.TextField(label="Nome de Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    error_message = ft.Text("", color=ft.colors.RED)




    # Função de verificar login
    def verificar_login(e):

        # Mensagem de erro
        if error_message.value:
            error_message.value = ""

        if not username_input.value or not password_input.value:
            page.add(ft.Text("Por favor, preencha todos os campos!", color=ft.colors.RED))
            page.add(error_message)
            page.update()
            return



    # Função de mostrar a página de login
    def show_login_page(e):
        page.controls.clear()  

        page.add(
            ft.Column(
                controls=[
                    ft.Text("Login", size=30),
                    username_input,
                    password_input,
                    error_message,
                    ft.ElevatedButton(text="Login", width=300, on_click=verificar_login),  
                    ft.TextButton(text="Esqueci a senha", width=300, on_click=recuperar_senha),
                    ft.TextButton(text="Criar conta", width=300, on_click=criar_conta),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            )
        )
        page.update()
        







    def criar_conta(e):

        new_username_input = ft.TextField(label="Nome de Usuário", width=300)
        new_password_input = ft.TextField(label="Senha", password=True, width=300)
        page.controls.clear()

        page.add(
            ft.Column(
                controls=[
                    ft.Text("Criar conta", size=30),
                    ft.Text("Por favor, insira um e-mail e uma senha válida!"),
                    new_username_input,
                    new_password_input,
                    error_message,
                    ft.ElevatedButton(text="Enviar", width=300, on_click=lambda e: verificar_login(e)), 
                    ft.TextButton(text="Voltar para login", width=300, on_click=show_login_page),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            )
        )












    def recuperar_senha(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Recuperação de Senha", size=30),
                    ft.Text("Por favor, insira seu e-mail para recuperação."),
                    ft.TextField(label="E-mail", width=300),
                    ft.ElevatedButton(text="Enviar", width=300),  # Botão para enviar solicitação de recuperação
                    ft.TextButton(text="Voltar para Login", on_click=show_login_page)  # Botão para voltar à página de login
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            )
        )

    # Inicia a função para mostrar o login
    show_login_page(None)

# Executando o app
ft.app(target=main)
