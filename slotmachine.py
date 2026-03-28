import random


def spin_row():
    symbols = ["💖", "🍌", "🍒", "👌", "🧊"]
    result = [random.choice(symbols) for _ in range(3)]

    return result


def print_row(row):
    print("|".join(row))


def get_payout(row, bet):
    if row[1] == row[0] == row[2]:
        if row[0] == "💖":
            return 2 * bet
        if row[0] == "🍌":
            return 3 * bet
        if row[0] == "🍒":
            return 4 * bet
        if row[0] == "👌":
            return 5 * bet
        if row[0] == "🧊":
            return 6 * bet

    return 0


def main():
    balance = 100

    print("----------------------")
    print("Welcom to Python Slots")
    print("Symbols: 💖 🍌 🍒 👌 🧊")
    print("----------------------")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinnin.....")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        if payout < 0:
            print("You lost")

        balance += payout

        play_again = input("Type Y for yes and N for no").upper()

        if play_again == "N":
            break

    print(f"You final balance is {balance}")


if __name__ == "__main__":
    main()
