from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def total_categories(self):
        return Category.category_count

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

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            average = total_price / len(self.__products)
            return average
        except ZeroDivisionError:
            print("Нет товаров в категории, поэтому средняя цена не может быть рассчитана.")
            return 0
