import flet as ft
import os

def main(page: ft.Page):
    page.title = "Pregunta importante bb"
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False

    # Configuración del contenido y los botones
    # (tu código aquí)

# Usa el puerto proporcionado por Render
port = int(os.environ.get("PORT", 8080))

# Usa un servidor web adecuado para Render
ft.app(target=main, view=ft.WEB_BROWSER, port=port)  # Esto ya debería funcionar bien en el entorno web
