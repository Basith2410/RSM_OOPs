# 4. Bank Class:
# You are building a banking application. You create a class called Bank that has a list of Account objects as an attribute. 
# You implement methods to add an account, remove an account, and calculate the total balance of all accounts in the bank.
# You create instances of Account named account1, account2, and account3. 
# You create a Bank object named myBank and add these accounts to the bank. 
# You perform operations like adding and removing accounts, and calculating the total balance.

class Account():
    def __init__(x, account_no, balance):
        x.account_no = account_no
        x.balance = balance


class Bank():
    def __init__(x):
        x.accounts = []

    def add_account(x, account):
        x.accounts.append(account)
        print("Account", account.account_no, "added to the bank.")

    def remove_account(x, account):
        x.accounts.remove(account)
        print("Account", account.account_no, "removed from the bank.")

    def calculate_balance(x):
        total_balance = sum(account.balance for account in x.accounts)
        return total_balance


account1 = Account("1B5A3", 20000)
account2 = Account("9K4H5", 30000)
account3 = Account("7F2Q1", 40000)

myBank = Bank()

myBank.add_account(account1)
myBank.add_account(account2)
myBank.add_account(account3)

total_balance = myBank.calculate_balance()
print("Total Balance in the bank:", total_balance)

myBank.remove_account(account3)

total_balance = myBank.calculate_balance()
print("Total Balance in the bank after account removal:", total_balance)
