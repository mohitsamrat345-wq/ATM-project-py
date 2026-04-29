import utils

def show_statement():
    print("\n--- Statement ---")
    for i in utils.transactions:
        print(i)
    print("Current Balance:", utils.balance)