import unittest
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from StudentDiscount import StudentDiscount
from Order import Order
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier


class TestDiscountStrategies(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Tech Supply", "supply@tech.com")
        self.product = PhysicalProduct("P001", "Laptop", 100.0, 10, 2.0, self.supplier)

    def test_no_discount(self):
        strategy = NoDiscount()
        self.assertEqual(strategy.apply(250.0), 250.0)

    def test_percentage_discount(self):
        strategy = PercentageDiscount(10.0)
        self.assertAlmostEqual(strategy.apply(250.0), 225.0)

    def test_bulk_discount_applied(self):
        strategy = BulkDiscount(200.0, 20.0)
        self.assertEqual(strategy.apply(250.0), 230.0)

    def test_bulk_discount_not_applied(self):
        strategy = BulkDiscount(200.0, 20.0)
        self.assertEqual(strategy.apply(150.0), 150.0)

    def test_student_discount(self):
        strategy = StudentDiscount(5.0)
        self.assertAlmostEqual(strategy.apply(200.0), 190.0)

    def test_order_with_strategy_and_set_discount(self):
        order = Order("ORD101", BulkDiscount(200.0, 20.0))
        order.add_order_line(self.product, 2)  # subtotal = 200.0
        self.assertEqual(order.calculate_total(), 180.0)
        # Change strategy dynamically
        order.set_discount(PercentageDiscount(10.0))
        self.assertAlmostEqual(order.calculate_total(), 180.0)
        order.set_discount(NoDiscount())
        self.assertEqual(order.calculate_total(), 200.0)


if __name__ == "__main__":
    unittest.main()
