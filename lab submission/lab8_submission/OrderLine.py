from Product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def display_line(self) -> None:
        print(f"  - {self.product.get_name()} ({self.product.get_product_id()}) x {self.quantity} @ ${format(self.product.get_price(), '.2f')} = ${format(self.calculate_subtotal(), '.2f')}")
        