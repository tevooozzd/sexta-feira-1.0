import flet as ft

def main(page: ft.Page):
    page.title = "SEXTA FEIRA (1.0) - LOGIN"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor=ft.colors.BLACK

    # Criando a área lateral esquerda
    lado_esquerdo = ft.Container(
        content=ft.Text('Lado Esquerdo', color=ft.colors.WHITE),
        bgcolor=ft.colors.GREY_900,
        width=350,
        height=650,  
        padding=20
    )

    # Criando o contêiner no meio 
    lado_cima = ft.Container(
        content=ft.Text('Parte Superior', color=ft.colors.WHITE),
        bgcolor=ft.colors.GREY_900,
        width=250,
        height=177,  # Ajustado para 10% a menos
        padding=20,
        margin=10
    )

    # Criando o contêiner no meio (centro) 
    lado_meio = ft.Container(
        content=ft.Text('Centro', color=ft.colors.WHITE),
        bgcolor=ft.colors.GREY_900,
        width=250,
        height=217,  # Ajustado para 10% a mais
        padding=20,
        margin=10
    )

    # Criando o contêiner na parte inferior 
    lado_baixo = ft.Container(
        content=ft.Text('Parte Inferior', color=ft.colors.WHITE),
        bgcolor=ft.colors.GREY_900,
        width=250,
        height=177,  
        padding=20,
        margin=10
    )

    # Criando a área lateral direita
    lado_direito = ft.Container(
        content=ft.Text('Lado Direito', color=ft.colors.WHITE),
        bgcolor=ft.colors.WHITE70,
        width=350,
        height=650,  
        padding=20
    )

    
    # Estrutura principal:o
    page.add(ft.Row([
        lado_esquerdo,
        ft.Column([
            lado_cima,
            lado_meio,
            lado_baixo
        ]),
        lado_direito
    ]))

# - Abrindo o app segundo a função main
ft.app(target=main)
