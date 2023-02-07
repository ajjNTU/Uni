# class Person:
#     '''A class person with name, address and contry'''
#     def __init__(self, full_name : str, addr : str, country : str):
#         self.name = full_name
#         self.addr = addr
#         self.country = country
class Purse:
    def __init__(self, purse_no : int, balance : float):
        self.purse_no = purse_no
        self.balance = balance

    def load_money(self, amount_to_load):
        self.balance = self.balance + amount_to_load

    def spend_money(self, amount_to_spend):
        if amount_to_spend <= self.balance:
            self.balance -= amount_to_spend
