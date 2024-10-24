import flet as ft

def sexta_feira(page):
    page.controls.clear()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Página da Sexta-Feira", size=30),
                ft.ElevatedButton(text="Teste", width=300),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )
    
    page.update()
