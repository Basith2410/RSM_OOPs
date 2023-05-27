# 2. Banking System Class Hierarchy:
# Nikunj is developing a banking system software. He creates a base class called Account with attributes account_number and balance. 
# He implements methods to deposit and withdraw money. He derives two subclasses: SavingsAccount and CheckingAccount. 
# In the SavingsAccount class, he adds an attribute interest_rate and a method calculate_interest() to calculate the interest earned. 
# In the CheckingAccount class, he adds an attribute overdraft_limit and a method apply_overdraft(). 
# He creates instances for a savings account named johnSavings and a checking account named janeChecking. 
# He performs operations like depositing, withdrawing, calculating interest, and applying overdraft on these accounts. 
# Assist Nikunj to finish this task.

class Account():
    def __init__(x, account_number, balance):
        x.account_number = account_number
        x.balance = balance

    def deposit(x, amount):
        x.balance += amount
        print("Deposited amount = ", amount)
    
    def withdraw(x, amount):
        if x.balance >= amount:
            x.balance -= amount
            print("Withdraw Amount = ", amount)
        else:
            print("Insuffiecient balance to withdraw amount")

class SavingsAccount(Account):
    def __init__(x, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        x.interest_rate = interest_rate

    def calculate_interest(x):
        interest_earned = x.balance * (x.interest_rate/100)
        print("Interest amount = ", interest_earned)

class CheckingAccount(Account):
    def __init__(x, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        x.overdraft_limit = overdraft_limit


    def apply_overdraft(x, amount):
        if amount <= x.balance + x.overdraft_limit:
            x.balance -= amount
            print("Overdraft Applied:", amount)
        else:
            print("Overdraft limit is exceeded, check once before you withdraw amount")

print("John's Savings Account")
johnSavings = SavingsAccount("11111", 5000, 3.5)
johnSavings.deposit(2000)
johnSavings.withdraw(1000)
johnSavings.calculate_interest()

print("\nJane's Checking Account")
janeChecking = CheckingAccount("22222", 3000, 1000)
janeChecking.deposit(1000)
janeChecking.withdraw(4000)
janeChecking.apply_overdraft(2000)