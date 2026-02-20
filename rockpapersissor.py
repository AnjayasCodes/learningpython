import random
options = ("rock", "paper", "scissor")
is_running = True
while is_running:

    player = "Name"
    computer = random.choice(options)

    while player.lower() not in options:
        player = input(
            "Please choose a option from (rock, paper, scissor)")

    print(f"Players Choice: {player}")
    print(f"Computers Choice: {computer}")
    if player == computer:
        print("No one won")
    elif player == "rock" and computer == "paper":
        print("You lost")
    elif player == "paper" and computer == "scissor":
        print("You lost")
    elif player == "scissor" and computer == "rock":
        print("You lost")
    else:
        print("You win")
        is_running = False
