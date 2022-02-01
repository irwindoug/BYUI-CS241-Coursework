'''
Assignment: Week 4 - Order Class
Brother Mellor, CS 241
Author: Doug Irwin
Summary: This class is for an order with an order ID and list of products.
'''

class Order:
    def __init__(self):
        self.id=""
        self.products = []

    def get_subtotal(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total

    def get_tax(self):
        return self.get_subtotal() * .065

    def get_total(self):
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print("Order: %s" % self.id)

        for product in self.products:
            product.display()

        print(("Subtotal: $%.2f") % self.get_subtotal())
        print(("Tax: $%.2f") % self.get_tax())
        print(("Total: $%.2f") % self.get_total())