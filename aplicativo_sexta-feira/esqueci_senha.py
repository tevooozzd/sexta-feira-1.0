import flet as ft

email_input = ft.TextField(label = 'E-mail', width=300)
error_message = ft.Text("", color=ft.colors.RED)


def esqueci_senha(page, login):

    def verificar_email(e):
        # Verifica se os campos estão vazios
        if not email_input.value:
            error_message.value = 'Por favor preencha todos os campos!'
            page.update()
            return
        else:
            # Se os campos estiverem preenchidos, faça algo (aqui está em branco)
            pass 
    error_message.value = ''

    page.controls.clear()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Recuperação de Senha", size=30),
                ft.Text("Por favor, insira seu e-mail para recuperação."),
                email_input,
                error_message,
                ft.ElevatedButton(text="Enviar", width=300, on_click=verificar_email),
                ft.TextButton(text="Voltar para Login", width=300, on_click=lambda e: login(page)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )
    page.update()
