from Product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size}MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."

    def to_dict(self):
        return {"type": "digital","id": self._product_id,"name": self._name,"price": self._price,"stock": self._stock,"download_size": self._download_size}
