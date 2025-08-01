import pytest
from Logica import FinanceManager
from Clases import Category

def test_new_movement_correctly():
    fm = FinanceManager()
    category = Category("food")
    fm.category.append(category)
    result = fm.new_movement(category,"diner","spent",4500.0)
    assert len(fm.movement) == 1

def test_new_movement_correctly_without_category():
    fm = FinanceManager()
    with pytest.raises(TypeError):
        fm.new_movement("diner","spent",4500.0)


def test_new_movement_raises_typeerror_when_amount_is_not_number():
    fm = FinanceManager()
    category = Category("food")
    with pytest.raises(TypeError):
        fm.new_movement(category, "dinner", "spent", "free")

def test_new_category():
    fm = FinanceManager()
    result = fm.new_category("food")
    assert len(fm.category) == 1