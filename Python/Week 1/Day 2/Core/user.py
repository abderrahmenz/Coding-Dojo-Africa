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


iheb_account = BankAccount(0.01,100)
yaya_account = BankAccount(0.04,1000)
iheb_account.deposit(30).deposit(150).deposit(200).withdraw(40).display_account_info()
yaya_account.deposit(300).deposit(250).withdraw(200).withdraw(150).withdraw(300).withdraw(100).display_account_info()