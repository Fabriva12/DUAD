import pytest
import csv
from Persistencia_de_datos import save_category_csv, save_movement_csv, charge_category_csv, charge_movements_csv
from Clases import Movement, Category
def test_save_and_charge_movement_csv_correctly():
    movement = [
        Movement("food", "apple", "spent", 50.0),
        Movement("salary", "work", "income", 1500.0)
    ]
    save_movement_csv(movement)
    resultado = charge_movements_csv()

    assert len(resultado) == 2
    assert resultado[1].category == "salary"


def test_save_and_charge_movement_csv_without_amount():
    with pytest.raises(TypeError):
        movement = [
        Movement("food", "apple", "spent", ),
        Movement("salary", "work", "income", )
    ]
        save_movement_csv(movement)
        resultado = charge_movements_csv()




def test_save_and_charge_category_csv_correctly():
    category = [
        Category("food"),
        Category("salary")
    ]
    save_category_csv(category)
    resultado = charge_category_csv()

    assert resultado[1].name == "food"
    assert resultado[2].name == "salary"

def test_save_and_charge_category_with_empty_category_():
    category = Category("")
    with pytest.raises(TypeError):
        save_category_csv(category)
        resultado = charge_category_csv()
