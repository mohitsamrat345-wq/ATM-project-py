import utils

def deposit(amount):
    utils.balance += amount
    utils.transactions.append("Deposited: " + str(amount))
    print("your money has been deposited successfully.\n Your New Balance is:", utils.balance)
 