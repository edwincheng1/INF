from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size: float = download_size

    @property
    def download_size(self) -> float:
        return self._download_size

    def get_download_size(self) -> float:
        return self._download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self._download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({"type": "digital","download_size": self._download_size})
        return base
