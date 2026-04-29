import utils 

def withdraw(amount):
    if amount > utils.balance:
        print("Insufficient balance!")
        return
    utils.balance -= amount
    utils.transactions.append("Withdrawn: " + str(amount))
    print("Withdrawn successfully. Remaining Balance:", utils.balance)   