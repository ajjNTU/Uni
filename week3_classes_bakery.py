# 1. Bakery
# Create a class called 'Invoice' that a bakery uses to represent an invoice for items sold. We assume this bakery
# takes large orders of one specific item only. Ex.: an order of 50 baguettes.
# An Invoice should include the following information: item type, quantity of item, a price per item and the date the
# order should be delivered.
#
# Create a new python file Invoice.py

# Create a class Bakery that contains a constructor __init__ that takes the information mentioned above as arguments.
class Invoice():
    """
    Class made if item_type, quantity, price_per_item, delivery_date to form Invoice class
    """
    def __init__(self, item_type, quantity, price_per_item, delivery_date):
        self.item_type = item_type
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.delivery_date = delivery_date
# Write a method named get_invoice() that calculates and returns the invoice amount.

# Add a docstring that describes your class.

# Add a string representation __str__ to your class.
    def __str__(self):
        return "Invoice Details: Item Type " + self.item_type + " # Quantity: " + str(self.quantity) + " # Price Per Item: " + str(self.price_per_item) + " # Delivery Date:" + self.delivery_date
# Add a method update_quantity(quantity) that updates that quantity of the item ordered. This method has one input
# parameter that represents the new quantity, and no output.
    def update_quantity(self,new_quantity):
        if new_quantity < 0:
            raise ValueError("Please enter positive number")
        else:
            self.quantity = new_quantity

# Add a method get_item() that returns the name of the item being ordered.
    def get_item(self):
        return "Item Type being invoiced: " + self.item_type

# Add a method get_quantity() that returns the quantity of the item being ordered.
    def get_quantity(self):
        return "Quantity being invoiced: " + str(self.quantity)
# We want to implement exception handling in method update_quantity() such that, If the new quantity is not positive,
# a ValueError exception is raised.

# Write a test function named invoice_test() that demonstrates class Invoice’s capabilities.
    def invoice_test(self):
        """
        return a file with the info for each order?
        email someone?
        with more classes like Stock could check order against that class?
            other classes customer info, supplier info?
        :return:
        """
        pass




order1 = Invoice('cake',50,5,"29/01/23")
print(order1.__doc__)
print(order1.get_item())
print(order1)
order1.update_quantity(150)
print(order1)
print(order1.get_quantity())
order1.update_quantity(-20)
