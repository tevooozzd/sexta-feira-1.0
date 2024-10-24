
import flet as ft

# Removendo as vírgulas que transformavam as variáveis em tuplas
username_input = ft.TextField(label="Nome de Usuário", width=300)
password_input = ft.TextField(label="Senha", password=True, width=300)
error_message = ft.Text("", color=ft.colors.RED)

def criar_conta(page, login):

    error_message.value = ""

    # Função de verificação de login
    def verificar_login(e):
        # Verifica se os campos estão vazios
        if not username_input.value or not password_input.value:
            error_message.value = 'Por favor preencha todos os campos!'
            page.update()
            return
        else:
            login(page)

    # Limpa a página para exibir a interface de criar conta
    page.controls.clear()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Criar conta", size=30),
                ft.Text("Por favor, insira um nome de usuário e uma senha válida!"),
                username_input,
                password_input,
                ft.ElevatedButton(text="Enviar", width=300, on_click=verificar_login),  # Corrigido para chamar `verificar_login`
                ft.TextButton(text="Voltar para login", width=300, on_click=lambda e: login(page)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )
    page.update()
