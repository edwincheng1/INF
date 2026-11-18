import unittest
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from OrderLine import OrderLine
from Supplier import Supplier


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Tech Supply", "supply@tech.com")

    def test_negative_or_zero_price_raises_error(self):
        with self.assertRaises(ValueError):
            PhysicalProduct("P001", "Lamp", 0.0, 10, 1.0, self.supplier)
        with self.assertRaises(ValueError):
            PhysicalProduct("P001", "Lamp", -10.0, 10, 1.0, self.supplier)

    def test_negative_stock_raises_error(self):
        with self.assertRaises(ValueError):
            DigitalProduct("D001", "App", 15.0, -5, 100.0, self.supplier)

    def test_update_stock_negative_raises_error(self):
        product = PhysicalProduct("P001", "Lamp", 25.0, 10, 1.0, self.supplier)
        with self.assertRaises(ValueError):
            product.update_stock(-1)

    def test_order_line_zero_or_negative_quantity_raises_error(self):
        product = PhysicalProduct("P001", "Lamp", 25.0, 10, 1.0, self.supplier)
        with self.assertRaises(ValueError):
            OrderLine(product, 0)
        with self.assertRaises(ValueError):
            OrderLine(product, -2)


if __name__ == "__main__":
    unittest.main()
