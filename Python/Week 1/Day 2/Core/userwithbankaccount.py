class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):

class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount 
        print(amount)
        return self
    def withdraw(self, amount):
        self.balance -= amount
        print(amount)
        return self
    def display_account_info(self):
        print(f"int_rate:{self.int_rate} \n balance:{self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self