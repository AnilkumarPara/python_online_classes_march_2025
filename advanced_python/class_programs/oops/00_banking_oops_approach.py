class BankAccount:
    def __init__(self, customer_name, balance=0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.customer_name} deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.customer_name} withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")
    def check_balance(self):
        print(f'{self.customer_name} is {self.balance}')



# Creating accounts for two people
alice_account = BankAccount("Alice")
bob_account = BankAccount("Bob")

# Alice and Bob performing transactions
alice_account.deposit(100)
alice_account.withdraw(30)
alice_account.check_balance()

bob_account.deposit(200)
bob_account.withdraw(50)
bob_account.check_balance()
balance=2000
