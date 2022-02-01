'''
Assignment: Week 4 - Order Class
Brother Mellor, CS 241
Author: Doug Irwin
Summary: This class is for a customer with a customer ID, name, and list of orders.
'''
class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        return len(self.orders)
    
    def get_total(self):
        total = 0
        for order in self.orders:
            total += order.get_total()
        return total
    
    def add_order(self, order):
        self.orders.append(order)
    
    def display_summary(self):
        print(("Summary for customer '%s':") % self.id)
        print(("Name: %s") % self.name)
        print(("Orders: %d") % self.get_order_count())
        print(("Total: $%.2f") % self.get_total())
    
    def display_receipts(self):
        print(("Detailed receipts for customer '%s':") % self.id)
        print(("Name: %s") % self.name)

        for order in self.orders:
            print()
            order.display_receipt()
                