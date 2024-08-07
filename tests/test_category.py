import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def create_product():
    return Product("Test Product", "Test Description", 10, 5)


def test_product_price_setter_positive():
    product = Product("Test", "Description", 10, 100)
    product.price = 15
    assert product.price == 15


def test_product_price_setter_negative():
    product = Product("Test", "Description", 10, 100)
    product.price = -5
    assert product.price == 10


def test_category_str_method(create_product):
    category = Category("Category3", "Description3", [create_product])
    assert str(category) == "Название категории: Category3, количество продуктов: 1 шт."


if __name__ == '__main__':
    pytest.main()
