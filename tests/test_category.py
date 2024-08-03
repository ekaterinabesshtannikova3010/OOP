import pytest
from src.product import Product
from src.category import Category


def test_category_initialization():
    products = [Product('Product 1', 'Description 1',23.99, 3), Product('Product 2', 'Description 2',48.59,5)]
    category = Category('Category Name', 'Category Description', products)

    assert category.name == 'Category Name'
    assert category.description == 'Category Description'
    assert category.products == products
    assert Category.product_count == 2
    assert Category.category_count == 1
#
# def test_category_initialization():
#     products = [Product('Product 1', 'Description 1',28.99, 6), Product('Product 2', 'Description 2',50.59,4)]
#     category = Category('Category Name', 'Category Description', products)
#
#     assert category.name == 'Category Name'
#     assert category.description == 'Category Description'
#     assert category.products == products
#     assert Category.product_count == 2
#     assert Category.category_count == 1

if __name__ == '__main__':
    pytest.main()