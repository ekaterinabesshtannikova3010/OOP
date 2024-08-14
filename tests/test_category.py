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
#
#
def test_category_str_method(create_product):
    category = Category("Category3", "Description3", [create_product])
    assert str(category) == "Название категории: Category3, количество продуктов: 1 шт."

def test_create_category_with_products():
    products = [
        Product("Product 1", "Description 1", 10.0, 5),
        Product("Product 2", "Description 2", 20.0, 10),
        Product("Product 3", "Description 3", 15.0, 3)
    ]
    category = Category("Electronics", "Electronics category", products)

    assert category.name == "Electronics"
    assert category.description == "Electronics category"
    assert category.products == (
        "Product 1, 10.0 руб. Остаток: 5 шт.\n"
        "Product 2, 20.0 руб. Остаток: 10 шт.\n"
        "Product 3, 15.0 руб. Остаток: 3 шт."
    )
    assert category.total_categories == 2
    assert category.product_count == 4


def test_add_product_to_category():
    products = [
        Product("Product 1", "Description 1", 10.0, 5),
        Product("Product 2", "Description 2", 20.0, 10)
    ]
    category = Category("Electronics", "Electronics category", products)

    new_product = Product("Product 3", "Description 3", 15.0, 3)
    category.add_product(new_product)

    assert category.products == (
        "Product 1, 10.0 руб. Остаток: 5 шт.\n"
        "Product 2, 20.0 руб. Остаток: 10 шт.\n"
        "Product 3, 15.0 руб. Остаток: 3 шт."
    )
    assert category.product_count == 7


def test_calculate_average_price():
    products = [
        Product("Product 1", "Description 1", 10.0, 5),
        Product("Product 2", "Description 2", 20.0, 10),
        Product("Product 3", "Description 3", 15.0, 3)
    ]
    category = Category("Electronics", "Electronics category", products)

    assert category.middle_price() == 15.0

    empty_category = Category("Empty Category", "Empty category", [])
    assert empty_category.middle_price() == 0


if __name__ == '__main__':
    pytest.main()
