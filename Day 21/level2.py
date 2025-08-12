from functools import reduce

class PersonAccount:
    def __init__(self, firstname = "", lastname = ""):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return reduce(lambda x, y : x + y, [i[0] for i in self.incomes]) if len(self.incomes) != 0 else 0
    def total_expense(self):
        return reduce(lambda x, y : x + y, [i[0] for i in self.expenses]) if len(self.expenses) != 0 else 0
    def account_info(self):
        return f"Your name is {self.firstname} {self.lastname}"
    def add_income(self, val, description):
        self.incomes.append([val, description])
    def add_expense(self, val, description):
        self.expenses.append([val, description])
    def account_balance(self):
        return self.total_income() - self.total_expense() 
