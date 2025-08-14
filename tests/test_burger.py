import pytest
from typing import List
from unittest.mock import Mock
from ..praktikum.burger import Burger

class TestBurger(object):

# Проверка инициализации класса
    def test_init_burger(self, burger):
        assert burger.bun == None
        assert burger.ingredients == []

# Проверка установки булочки
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

# Проверка добавления ингридиентов в бургер
    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

# Проверка удаления ингридиента из бургера
    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

# Проверка удаления ингридиента с некорректным индексом
    def test_remove_invalid_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(3)

# Проверка перемещения ингридиентов
    def test_move_ingredient(self, burger):
        ingredient1_mock = Mock()
        ingredient1_mock.get_name.return_value = "Cheese"
        ingredient1_mock.get_type.return_value = "FILLING"
        ingredient1_mock.get_price.return_value = 25.0
        ingredient2_mock = Mock()
        ingredient2_mock.get_name.return_value = "Red Hot Chili Peppers"
        ingredient2_mock.get_type.return_value = "FILLING"
        ingredient2_mock.get_price.return_value = 150.0
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.move_ingredient(1,0)
        assert burger.ingredients == [ingredient2_mock, ingredient1_mock]

# Проверка расчёта стоимости бургера
    @pytest.mark.parametrize("ingredients, expected_price", [
        ([("FILLING", "Cheese", 70.0), ("SAUCE", "Ketchup", 25.0)], 195.0),
        ([("FILLING", "Red Hot Chili Peppers", 20.0), ("FILLING", "Tomato", 30.0), ("SAUCE", "BBQ", 20.0)], 170.0)
    ])
    def test_get_price(self, burger, bun, ingredients, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredients:
            ingredient_mock = Mock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

# проверка генерации рецепта
    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        excepted_receipt: List[str] = [f'(==== {bun.get_name()} ====)']
        excepted_receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
        excepted_receipt.append(f'(==== {bun.get_name()} ====)\n')
        excepted_receipt.append(f'Price: {burger.get_price()}')

        assert burger.get_receipt() == '\n'.join(excepted_receipt)