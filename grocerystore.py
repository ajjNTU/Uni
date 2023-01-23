# 3. Grocery Store
# Consider the following list that contains products from a grocery store and their respective expiry date which ranges
# between today and tomorrow. Information on products is stored in the form of a dictionary.
import string

products = [
{'milk': '1', 'expiration_date': 'today', 'price': 1.45},
{'organic milk': '2', 'expiration_date': 'tomorrow', 'price': 2.15},
{'filtered milk - whole': '3', 'expiration_date': 'tomorrow', 'price': 1.95},
{'filtered milk - skimmed': '4', 'expiration_date': 'today', 'price': 1.85},
]
# 1. Write a program that displays each product alongside its expiration date.
def productandexp():
    products = [
        {'milk': '1', 'expiration_date': 'today', 'price': 1.45},
        {'organic milk': '2', 'expiration_date': 'tomorrow', 'price': 2.15},
        {'filtered milk - whole': '3', 'expiration_date': 'tomorrow', 'price': 1.95},
        {'filtered milk - skimmed': '4', 'expiration_date': 'today', 'price': 1.85},
    ]
    i = 0
    while i < len(products):
        print(string.capwords(list(dict(products[i]).keys())[0] + " Expires " + dict(products[i])['expiration_date']))
        i += 1


productandexp()


# 2. The store wants to apply a discount of 30% to items that are expiring today. Write a function discount(product,
# expiration_date) that returns the price of an item after discount. product should be in the form of a dictionary.
def discount(expiration: str = "today", product: dict = [
{'milk': '1', 'expiration_date': 'today', 'price': 1.45},
{'organic milk': '2', 'expiration_date': 'tomorrow', 'price': 2.15},
{'filtered milk - whole': '3', 'expiration_date': 'tomorrow', 'price': 1.95},
{'filtered milk - skimmed': '4', 'expiration_date': 'today', 'price': 1.85},
]):
    for i in range(len(product)):
        if products[i]['expiration_date'] == expiration:
            print(string.capwords(list(dict(product[i]).keys())[0]) + " Discounted Price: " + str(float(dict(product[i])['price'])*0.7))
        else:
            print(string.capwords(list(dict(product[i]).keys())[0]) + " Price: " + str(float(dict(product[i])['price'])))

print("")
discount()
print("")
discount("tomorrow")

# 3. Extend your program to display the items and their prices after discount.

# print(dict(products[1])['price'])
# print(products)
# print(products[1])
# print(len(products[1]))
# print(len(products))
# print(list(dict(products[1]).keys())[0])


