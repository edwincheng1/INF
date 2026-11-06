from Product import Product
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight}kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self._weight * 5.0

    def to_dict(self):
        return {"type": "physical","id": self._product_id,"name": self._name,"price": self._price,"stock": self._stock,"weight": self._weight}
