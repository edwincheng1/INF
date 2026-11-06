class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def search_product(self, product_id):
        for product in self._products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("---------------------------------------------")
        if not self._products:
            print("Inventory is empty.")
        else:
            for product in self._products:
                product.display_information()
        print("---------------------------------------------\n")

    def get_all_products(self):
        return self._products
