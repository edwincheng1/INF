from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def update_stock(self, quantity):
        self._stock = quantity

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${format(self._price, '.2f')} | Stock: {self._stock}", end=" | ")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def to_dict(self):
        return {"id": self._product_id,"name": self._name,"price": self._price,"stock": self._stock}
