from src.product import Product
import pytest


@pytest.fixture
def create_product():
    return Product("Test Product", "Test Description", 10, 5)


def test_price_setter_negative():
    product = Product("Test Product", "Description", 10.0, 5)
    product.price = -5
    assert product.price == 10.0


def test_price_setter_zero():
    product = Product("Test Product", "Description", 10.0, 5)
    product.price = 0
    assert product.price == 10.0


def test_price_setter_positive():
    product = Product("Test Product", "Description", 10.0, 5)
    product.price = 15.0
    assert product.price == 15.0


def test_product_add_method():
    product1 = Product("Product1", "Description1", 20, 3)
    product2 = Product("Product2", "Description2", 15, 2)
    total_cost = product1 + product2
    assert total_cost == 90


if __name__ == "__main__":
    pytest.main()
