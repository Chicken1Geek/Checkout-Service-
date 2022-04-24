

class Product:

    def __init__(self, barcode, name, desc, price):
        self.barcode = barcode
        self.name = name
        self.desc = desc
        self.price = price

    def printDetails(self):
        return f"{self.name},{self.desc}- &{self.price}"

    def __eq__(self, other_product):
        if self.barcode == other_product.barcode:
            return True
        else:
            return False
