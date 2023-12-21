class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here

    def display_account_info(self):
        # print("Balance: " + self.balance)
        print(f"Balance: {self.balance}")
        return self
        # your code here

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
        # your code here


jim_account = BankAccount()
shon_account = BankAccount()

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
print(
    jim_account.deposit(235)
    .deposit(331)
    .deposit(248)
    .withdraw(60)
    .yield_interest()
    .display_account_info()
)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
print(
    shon_account.deposit(2000)
    .deposit(4000)
    .withdraw(60)
    .withdraw(100)
    .withdraw(1600)
    .withdraw(3)
    .yield_interest()
    .display_account_info()
)
