import PySimpleGUI as sg
sg.theme('Material2') 
from Logica import FinanceManager
from Persistencia_de_datos import save_category_csv, save_movement_csv, charge_category_csv, charge_movements_csv

def category_window(manager):

    layout = [
        [sg.Text("Nombre de la nueva categoría:"), sg.Input(key="nombre")],
        [sg.Button("Agregar"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Agregar Categoría", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break
        if event == "Agregar":
            name= values["nombre"]
            if name:
                manager.new_category(name)
                save_category_csv(manager.category)
                sg.popup("Categoría agregada.")
                break
            else:
                sg.popup_error("El nombre no puede estar vacío.")
    window.close() 

def movement_window(manager, type):
    if not manager.category:
        sg.popup_error("No hay categorías disponibles. Agrega una primero.")
        return

    layout = [
        [sg.Text("Título:"), sg.Input(key="titulo")],
        [sg.Text("Monto:"), sg.Input(key="monto")],
        [sg.Text("Categoría:"), sg.Combo([cat.name for cat in manager.category], key="categoria")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    window = sg.Window(f"Agregar {type}", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break
        if event == "Guardar":
            try:
                title = values["titulo"]
                amount = float(values["monto"])
                category = values["categoria"]
                if not title or not category:
                    sg.popup_error("Todos los campos son obligatorios.")
                else:
                    manager.new_movement(category,title,type, amount)
                    save_movement_csv(manager.movement)
                    sg.popup(f"{type} agregado.")
                    break
            except ValueError:
                sg.popup_error("El monto debe ser un número.")
    window.close()

manager= FinanceManager()
manager.category = charge_category_csv()
manager.movement = charge_movements_csv()


def main_window():
    encabezado = ["Título", "Tipo", "Categoría", "Monto"]

    layout = [
        [sg.Text("Movimientos Registrados",)],
        [sg.Table(values=[],
        headings=encabezado,
        key="tabla",
        expand_x=True,
        expand_y=True,
        auto_size_columns=True,
        justification="left",
        num_rows=10)],
        [sg.Button("Agregar Categoría"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso"), sg.Button("Salir")]
    ]

    window = sg.Window("Gestor de Finanzas", layout, size=(600, 400), resizable=True, finalize=True)

    while True:
        datos_tabla = [[m.title, m.type, m.category, m.amount] for m in manager.movement]
        window["tabla"].update(values=datos_tabla)

        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Salir"):
            break
        elif event == "Agregar Categoría":
            category_window(manager)
        elif event == "Agregar Gasto":
            movement_window(manager, type="Gasto")
        elif event == "Agregar Ingreso":
            movement_window(manager, type="Ingreso")

    window.close()



main_window()