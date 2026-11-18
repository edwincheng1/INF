from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for i, line in enumerate(self.order_lines):
            if line.product.get_product_id().upper() == product_id.upper():
                del self.order_lines[i]
                return True
        return False

    def calculate_subtotal_raw(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def calculate_total(self) -> float:
        total = self.calculate_subtotal_raw()
        return self.discount.apply(total)

    def display_order(self) -> None:
        print(f"\nOrder ID: {self.order_id}")
        print("---------------------------------------------")
        for line in self.order_lines:
            line.display_line()
        raw_total = self.calculate_subtotal_raw()
        discounted_total = self.calculate_total()
        discount_saved = raw_total - discounted_total
        print(f"Subtotal: ${format(raw_total, '.2f')}")
        print(f"Discount Applied ({self.discount.__class__.__name__}): -${format(discount_saved, '.2f')}")
        print(f"Final Total Order Amount: ${format(discounted_total, '.2f')}")
        print("---------------------------------------------\n")
