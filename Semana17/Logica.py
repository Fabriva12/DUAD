from Clases import Movement, Category
import PySimpleGUI as sg
from Persistencia_de_datos import  save_movement_csv , charge_movements_csv, save_category_csv
class FinanceManager:
    def __init__(self):
        self.category = []    
        self.movement = []   

    def new_category(self,name):
        new_category = Category(name)
        self.category.append(new_category)
        return self.category

    def new_movement(self, category, title, movement_type, amount):
        new_movement = Movement(category, title, movement_type, amount,)
        self.movement.append(new_movement)
        return self.movement

def window_create_and_save_movement(manager, title, amount, category, type):
    try:
        amount = float(amount)
        if not title or not category or amount < 1:
            sg.popup_error("Todos los campos son obligatorios.")
            return False
        manager.new_movement(category, title, type, amount)
        save_movement_csv(manager.movement)
        sg.popup(f"{type} agregado.")
        return True
    except ValueError:
        sg.popup_error("El monto debe ser un número.")
        return False

def window_create_and_save_category(manager, name): 
    if not name:
        sg.popup_error("El nombre no puede estar vacío.")
        return False
    nombres_existentes = [cat.name.lower() for cat in manager.category]
    if name.lower() in nombres_existentes:
        sg.popup_error("La categoría ya existe.")
        return False
    manager.new_category(name)
    save_category_csv(manager.category)
    sg.popup("Categoría agregada.")
    return True