from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        return self._price

    @price.setter
    @abstractmethod
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @abstractmethod
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @abstractmethod
    def __add__(self, other):
        if isinstance(other, BaseProduct):
            total_cost = (self.price * self.quantity) + (other.price * other.quantity)
            return total_cost
        return NotImplemented

    @classmethod
    @abstractmethod
    def new_product(cls, product_info: dict):
        return cls(
            name=product_info.get("name"),
            description=product_info.get("description"),
            price=product_info.get("price"),
            quantity=product_info.get("quantity")
        )

    @classmethod
    @abstractmethod
    def add_product(cls, product_list, new_product):
        if isinstance(new_product, cls):
            product_list.append(new_product)
            print(f"{new_product.name} has been added to the category.")
        else:
            print("Only instances of the 'Product' class or its subclasses can be added to this category.")


class ProductCreationInfo:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.print_creation_info()

    def print_creation_info(self):
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами: name={self.name},"
            f" description={self.description}, price={self.price}, quantity={self.quantity}")


class Product(ProductCreationInfo, BaseProduct):
    def __init__(self, name, description, price, quantity):
        ProductCreationInfo.__init__(self, name, description, price, quantity)
        BaseProduct.__init__(self, name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, BaseProduct):
            total_cost = (self.price * self.quantity) + (other.price * other.quantity)
            return total_cost
        return NotImplemented

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(
            name=product_info.get("name"),
            description=product_info.get("description"),
            price=product_info.get("price"),
            quantity=product_info.get("quantity")
        )

    @classmethod
    def add_product(cls, product_list, new_product):
        if isinstance(new_product, cls):
            product_list.append(new_product)
            print(f"{new_product.name} has been added to the category.")
        else:
            print("Only instances of the 'Product' class or its subclasses can be added to this category.")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
