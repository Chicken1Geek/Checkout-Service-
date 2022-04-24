
from Product_Class import Product
import datetime


class CheckoutRegister:
    def __init__(self):
        self.products = []
        self.shopping_cart = []
        self.amount_paid = 0
        self.amount_due = 0
        # open products.txt for reading
        file = open("products.txt", "r")
        # read each line from file
        # spilt each line into barcode, name,desc, price
        # create a Product object with above values
        # add this product to the products list
        for line in file:
            barcode, name, desc, price = line.strip().split(" ")
            product = Product(barcode, name, desc, float(price))
            self.products.append(product)
        file.close()

    def scan_item(self, barcode):  # scan item from barcode if correct barcode them print product details--------------
        for product in self.products:
            if product.barcode == barcode:  # use barcode to find the product object from the product[]
                self.shopping_cart.append(product)  # add product to shopping cart
                self.amount_due += product.price
                return product  # return products
        return None  # else product not found return none

    def accept_payment(self, get_amount_to_pay):  # accept payment
        self.amount_due -= get_amount_to_pay
        self.amount_paid += get_amount_to_pay
        return self.amount_due

    def get_amount_to_pay(self):  # get amount to pay
        get_amount_to_pay = 0
        for p in self.shopping_cart:
            get_amount_to_pay += p.price
            return get_amount_to_pay  # return the total amount of all products in the shopping_cart

    # print receipt
    def print_receipt(self, payment_amount):  # print receipt out
        print("------FINAL RECEIPT-------")
        print(self.shopping_cart)  # print out shopping cart items.
        print(f"Total amount due: ", {payment_amount})
        print(f"Amount received:, {self.amount_paid} ")  # amount received and how much left to pay if any.
        print(f"Balance given: , {self.accept_payment}")  # accept payment amount

        #  save transaction date to transaction file then close file
    def save_transaction(self, date, barcode):
        if self.accept_payment is True:
            file = open("transactionfile_assignment#3_PYI_GEorgiaBatten.txt", "a")
            # write amount_to_pay , barcode , date to file here
            file.write(str(barcode, date))
            # save transaction datetime to file here
            file.write(str(datetime.datetime.today()))
            file.close()
        else:
            print("ERROR!! Transaction cant be saved!!")
