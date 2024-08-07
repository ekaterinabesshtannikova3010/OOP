from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        output = ""
        for product in self.__products:
            output += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return output.rstrip()

    def __str__(self):
        return f"Название категории: {self.name}, количество продуктов: {Category.product_count} шт."
