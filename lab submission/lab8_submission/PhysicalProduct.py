from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self._weight: float = weight

    @property
    def weight(self) -> float:
        return self._weight

    def get_weight(self) -> float:
        return self._weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self._weight}kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self._weight * 5.0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({"type": "physical","weight": self._weight})
        return base