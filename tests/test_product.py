from src.product import Product
import pytest


def test_product_initialization():
    """Тестируем правильную инициализацию объекта продукта"""
    product = Product("Test Product", "This is a test product", 19.99, 10)

    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 19.99
    assert product.quantity == 10


def test_product_creation():
    """Тестируем метод product_creation"""
    product_info = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 29.99,
        "quantity": 5
    }

    product = Product.product_creation(product_info)

    assert product.name == "New Product"
    assert product.description == "This is a new product"
    assert product.price == 29.99
    assert product.quantity == 5


def test_product_creation_with_missing_fields():
    """Тестируем метод product_creation с пропущенными полями"""
    product_info = {
        "name": "Incomplete Product",
        # Описание отсутствует
        "price": 15.0,
        "quantity": 8
    }

    product = Product.product_creation(product_info)

    assert product.name == "Incomplete Product"
    assert product.description is None  # По умолчанию должно быть None
    assert product.price == 15.0
    assert product.quantity == 8



if __name__ == "__main__":
    pytest.main()
