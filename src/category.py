from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        self.product_count += 1
