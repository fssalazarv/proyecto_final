from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
## importando funciones de controlador

from controller.function import *
from config.app import *
## import reports

from controller.reports import *
from controller.reports_categoria import *

def menu(app: App):
    console = Console()

    while True:
        # Crear el texto del menú con colores y emojis
        menu_text = Text()
        menu_text.append("\n📊 [bold cyan]Proyecto Datux[/bold cyan]\n", style="underline bold")
        menu_text.append("\n[1] 🟢 Ingestar Data\n", style="green")
        menu_text.append("[2] 📈 Reporte de Ventas\n", style="blue")
        menu_text.append("[3] 📊 Reporte de Ventas por Categoría\n", style="magenta")
        menu_text.append("[4] ❌ Salir\n", style="red")

        # Mostrar el menú en un panel
        console.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

        # Solicitar opción al usuario
        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3", "4"], default="4")

        # Manejar la opción elegida
        if opcion == "1":
            IngestDataProducts(app)
        elif opcion == "2":
            GenerateReportVentas(app)
        elif opcion == "3":
            GenerateReportVentasCategoria(app)  # Nueva función para reporte por categoría
        elif opcion == "4":
            break  # Sale del bucle y 
