import unittest
from ProductFactory import ProductFactory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier


class TestProductFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Tech Supply", "supply@tech.com")

    def test_create_physical_product(self):
        product = ProductFactory.create("physical", "P001", "Desk Lamp", 25.0, 10, self.supplier, 1.5)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_product_id(), "P001")
        self.assertEqual(product.get_weight(), 1.5)

    def test_create_digital_product(self):
        product = ProductFactory.create("digital", "D001", "Photo Editor", 49.9, 100, self.supplier, 250.0)
        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_product_id(), "D001")
        self.assertEqual(product.get_download_size(), 250.0)

    def test_create_unknown_type_raises_value_error(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier)


if __name__ == "__main__":
    unittest.main()
