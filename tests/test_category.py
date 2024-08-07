import pytest
from src.product import Product


def test_product_price_setter_positive():
    product = Product("Test", "Description", 10, 100)
    product.price = 15
    assert product.price == 15


def test_product_price_setter_negative():
    product = Product("Test", "Description", 10, 100)
    product.price = -5
    assert product.price == 10


if __name__ == '__main__':
    pytest.main()
