
from Checkout_Register_Class import CheckoutRegister
import datetime


def main():
    _continue = True
    scan_another = "Y"
    cr = CheckoutRegister()  # create instance of CheckoutRegister
    while _continue:
        while scan_another == "Y":
            barcode = input("Please enter the barcode: ")
            product = cr.scan_item(barcode)
            if product is None:
                print("ERROR!! – scanned barcode is incorrect")
            else:
                print(product.printDetails())
            scan_another = str.capitalize(input("Would you like to scan another item:"))

        while True:
            print(f"Payment due:${cr.amount_due} ", end=" ")
            payment_amount = float(input("Please enter an amount to pay:"))
            amount_due = cr.accept_payment(payment_amount)
            if amount_due <= 0:
                print("saving transaction")
                # save transaction to file here
                file = open("transactionfile_assignment#3_PYI_GEorgiaBatten.txt", "a")
                file.write(str(datetime.datetime.today()))
                file.close()
                # loop back to line 21
                # else: break from while loop

            # print receipt
                print("------FINAL RECEIPT-------")
                print(product.printDetails())
                print(f"Total amount due:, {payment_amount}")
                print(f"Amount received:, {cr.amount_paid} ")  # amount received and how much left to pay if any.
                print(f"Balance given: , {cr.amount_paid}")  # accept payment amount
                return

            #  clear shopping_cart[]
            cr.shopping_cart.remove(product)


main()
