from Product import Product
from OrderLine import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for i, line in enumerate(self.order_lines):
            if line.product.get_product_id().upper() == product_id.upper():
                del self.order_lines[i]
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display_order(self) -> None:
        print(f"\nOrder ID: {self.order_id}")
        print("---------------------------------------------")
        for line in self.order_lines:
            line.display_line()
        print(f"Total Order Amount: ${format(self.calculate_total(), '.2f')}")
        print("---------------------------------------------\n")
