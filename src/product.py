
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(
            name=product_info.get("name"),
            description=product_info.get("description"),
            price=product_info.get("price"),
            quantity=product_info.get("quantity")
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value
