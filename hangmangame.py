import random

words = ["Pokemon", "Life", "art", "squirtle"]
life = 3
random_word = random.choice(words).lower()
Word_length = len(random_word)
Word = []
for x in range(Word_length):
    Word.append(" _")

print("Word =", end=" ")
for letter in Word:
    print(letter, end=" ")
print()


while life > 0:
    guess = input("Enter a guess letter for the word")
    if guess.lower() not in random_word:
        life -= 1
        print("Wrong letter")
        print(f"life: {life}")
        continue

    for i in range(len(random_word)):
        if random_word[i] == guess:
            Word[i] = " " + guess.lower()

    print("Result=", end=" ")
    for letter in Word:
        print(letter, end=" ")
    print()

    result = "".join(Word).replace(" ", "")

    if result == random_word:
        print("You won")
        break

if life == 0:
    print("You lost")
