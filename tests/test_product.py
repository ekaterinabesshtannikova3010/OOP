from src.product import BaseProduct, Product, ProductCreationInfo, Smartphone, LawnGrass
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


def test_new_product():
    product_info = {"name": "Test", "description": "Test description", "price": 10, "quantity": 5}
    product = Product.new_product(product_info)
    assert product.name == "Test"
    assert product.description == "Test description"
    assert product.price == 10
    assert product.quantity == 5


def test_price_setter():
    p = Product("Test", "", 10, 5)
    p.price = -1
    assert p.price == 10


def test_smartphone_init():
    smartphone = Smartphone("Smartphone1", "", 500, 3, "high", "model1", "16GB", "black")
    assert smartphone.efficiency == 'high'


def test_lawngrass_init():
    grass = LawnGrass("Lawn Grass1", "", 20, 7, "USA", "2 weeks", "green")
    assert grass.country == "USA"


def test_product_creation_info():
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    assert isinstance(product, ProductCreationInfo)
    assert isinstance(product, BaseProduct)
    assert product.name == "Продукт1"
    assert product.description == "Описание продукта"
    assert product.price == 1200
    assert product.quantity == 10


def test_smartphone_creation_info():
    smartphone = Smartphone("iPhone 12", "Новейший смартфон", 79999, 50, 0.95, "iPhone 12", 128, "Черный")
    assert isinstance(smartphone, ProductCreationInfo)
    assert isinstance(smartphone, BaseProduct)
    assert smartphone.name == "iPhone 12"
    assert smartphone.description == "Новейший смартфон"
    assert smartphone.price == 79999
    assert smartphone.quantity == 50


def test_lawn_grass_creation_info():
    lawn_grass = LawnGrass("Газонная трава", "Высококачественная газонная трава", 500, 20, "Россия", 14, "Зеленый")
    assert isinstance(lawn_grass, ProductCreationInfo)
    assert isinstance(lawn_grass, BaseProduct)
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Высококачественная газонная трава"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20


if __name__ == "__main__":
    pytest.main()
