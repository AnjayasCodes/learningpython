def Show_Balance(balance):
    print("************")
    print(f"Your balance is {balance: .2f}")
    print("************")


def deposit(balance):
    print("************")
    amount = float(input("Enter an amount to be deposited"))
    if amount < 0:
        print("You cannot deposit this amount")
        print("************")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("How much money do you want to withdraw"))
    if amount > balance:
        print("You dont have suffincinet amount of money")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Progress")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choise 1-4")

        if choice == "1":
            Show_Balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thanks for using our service")
            is_running = False
        else:
            print("Invalid Entry")


if __name__ == "__main__":
    main()
