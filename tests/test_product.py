from src.product import Product
import pytest

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


if __name__ == "__main__":
    pytest.main()
