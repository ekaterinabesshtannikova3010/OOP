from src.product import Product, Smartphone, LawnGrass
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


if __name__ == "__main__":
    pytest.main()
