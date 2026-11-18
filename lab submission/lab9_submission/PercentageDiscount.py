from DiscountStrategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1.0 - (self.percentage / 100.0))
