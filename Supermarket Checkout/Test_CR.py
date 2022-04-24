
import unittest


class CheckoutRegister_Test(unittest.TestCase):
    def setUp(self):
        self.product = "456", "Bread", "500g", 2.50

    def test_Scan_item(self):
        self.assertIn('456', self.product)

    def test_accept_payment(self):
        self.accept_payment = "5"
        self.assertEqual('5', self.accept_payment)

    def test__init__(self):
        self.barcode = "123", "456", "789"
        self.assertIn("456", self.barcode)

    if __name__ == '__main__':
        unittest.main()
