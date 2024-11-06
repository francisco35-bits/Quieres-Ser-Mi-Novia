import flet as ft
import random

def main(page: ft.Page):
    page.title = "Pregunta importante bb"
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False

    margen_inferior = 100
    margen_lateral = 120
    movimiento_minimo = 50

    def mover_boton_no(e):
        max_top = page.window_height - margen_inferior
        max_left = page.window_width - margen_lateral

        top_actual = btn_no.top
        left_actual = btn_no.left

        nuevo_top, nuevo_left = top_actual, left_actual
        while abs(nuevo_top - top_actual) < movimiento_minimo or abs(nuevo_left - left_actual) < movimiento_minimo:
            nuevo_top = random.randint(0, int(max_top))
            nuevo_left = random.randint(0, int(max_left))

        btn_no.top = nuevo_top
        btn_no.left = nuevo_left
        page.update()

    def mostrar_respuesta(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Sabía que dirías que sí, bb. Ahora desnúdate🥵"),
            actions=[ft.ElevatedButton("Cerrar", on_click=lambda e: page.window_close())]
        )
        page.dialog.open = True
        page.update()

    # Crear botones
    btn_si = ft.ElevatedButton("Sí", on_click=mostrar_respuesta, width=100)
    btn_no = ft.ElevatedButton("No", width=100, on_hover=mover_boton_no)

    # Colocar los botones en un Stack
    stack = ft.Stack(
        [
            btn_si,
            btn_no,
        ],
        width=400,
        height=300,
    )

    btn_si.top = 100
    btn_si.left = 50

    btn_no.top = 100
    btn_no.left = 200

    # Agregar el contenido a la página
    page.add(
        ft.Column(
            [
                ft.Text("¿Quieres ser mi novia bb?", size=30, weight=ft.FontWeight.BOLD),
                stack,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
