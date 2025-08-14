import pytest
from ..praktikum.database import Database
from unittest.mock import Mock
from ..praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "very big bun"
    mock_bun.get_price.return_value = 50.00
    return mock_bun

@pytest.fixture
def ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'Caesar'
    mock_ingredient.get_price.return_value = 15.00
    mock_ingredient.get_type.return_value = 'SAUCE'
    return mock_ingredient

