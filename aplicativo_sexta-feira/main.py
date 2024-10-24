import flet as ft
from login import login
from criar_conta import criar_conta
from esqueci_senha import esqueci_senha
from sexta_feira import sexta_feira

def main(page: ft.Page):
    page.title = "SEXTA-FEIRA 1.0"
    page.vertical_alignment = ft.MainAxisAlignment.START

    def pagina_login_main(e=None):
        login(page, pagina_criar_conta, pagina_esqueci_senha, pagina_sexta_feira)

    def pagina_criar_conta(e=None):
        criar_conta(page, pagina_login_main)

    def pagina_esqueci_senha(e=None):
        esqueci_senha(page, pagina_login_main)
    
    def pagina_sexta_feira(e=None):
        sexta_feira(page)

    pagina_login_main(None)

ft.app(target=main)

