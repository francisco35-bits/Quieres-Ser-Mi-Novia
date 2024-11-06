import os
port = int(os.environ.get("PORT", 8080))
ft.app(target=main, view=ft.WEB_BROWSER, port=port)
