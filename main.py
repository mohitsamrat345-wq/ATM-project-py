from deposit_money import deposit
from withdraw_money import withdraw
from display_balance import display_balance
from statement import show_statement


while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        amount = int(input("Enter amount you want to deposit: "))
        deposit(amount)
    elif choice == "3":
        amount = int(input("Enter amount you want to withdraw: "))
        withdraw(amount)
    elif choice == "4":
        show_statement()
    elif choice == "5":
        print("Goodbye! Thank you for using our ATM service!")
        break
    else:
        print("Invalid choice!")