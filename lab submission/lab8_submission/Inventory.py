from Product import Product


class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: str) -> bool:
        for i, product in enumerate(self.products):
            if product.get_product_id().upper() == product_id.upper():
                del self.products[i]
                return True
        return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("---------------------------------------------")
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                product.display_information()
        print("---------------------------------------------\n")

    def get_all_products(self) -> list[Product]:
        return self.products
