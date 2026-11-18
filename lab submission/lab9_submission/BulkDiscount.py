from DiscountStrategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount cannot be negative.")
        self.threshold: float = threshold
        self.amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return max(0.0, total - self.amount)
        return total
