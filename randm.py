import random
highest_num = 100
lowest_num = 1

num = random.randint(lowest_num, highest_num)
print("++++++Guess The Number Game++++++")

score = 0
is_running = True
tries = 0
guesses = []
while is_running:
    guess = (input(f"Enter the number from {lowest_num} to {highest_num}"))
    tries += 1
    guesses.append(guess)

    if guess.isdigit():
        guess = int(guess)
        if guess > highest_num or guess < lowest_num:
            print(
                f"The number must be from in range of {lowest_num} to {highest_num}")
        elif guess > num:
            print("The entered number is too big")
        elif guess < num:
            print("The entered number is too low")
        else:
            print("Correct guess")
            is_running = False

    else:
        print("You must enter a number  in range 1 to 100")

print(f"Number of guesses: {tries}")
for guess in guesses:
    print(guess, end=" ")
