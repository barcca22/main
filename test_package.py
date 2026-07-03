from unittest import TestCase
from package import Package

class TestPrice(TestCase):
    def test_light_package(self):
        p= Package("A", 0.25, "nedoručeno")
        price = p.delivery_price()
        self.assertEqual(price, 129)
    def test_medium_package(self):
        p= Package("A", 15, "nedoručeno")
        price = p.delivery_price()
        self.assertEqual(price, 159)
class TestInfo(TestCase):
    def test_address(self):
        p = Package("Květinová 856/22, Bolatice", 5, "nedoručeno")
        info = p.get_info()
        self.assertIn("22", info)
