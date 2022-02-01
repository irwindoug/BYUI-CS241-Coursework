'''
Assignment: Week 4 - Product Class
Brother Mellor, CS 241
Author: Doug Irwin
Summary: This class is for a product with an item ID, name, price, and quantity left of the product.
'''

class Product:

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return (self.quantity * self.price)

    def display(self):
        print(("%s (%i) - $%.2f") % (self.name, self.quantity, self.get_total_price()))