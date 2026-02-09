questions = ("What  the color of Mars",
             "Who is the biggest Planet",
             "Who is the PrimeMinister of Nepal")

choices = (
    ("A. Red", "B. Blue", "C. Green"),
    ("A. Earth", "B. Jupiter", "C. Mars"),
    ("A. KP Oli", "B. Sher Bahadur Deuba", "C. Pushpa Kamal Dahal")
)

answer = ("A", "B", "C")
guesses = []
question_num = 0
score = 0
guesses = []


for question in questions:
    print("------------------")
    print(question)
    for choice in choices[question_num]:
        print(choice)

    guess = input("Choose what you think is the answer").upper()
    guesses.append(guess)
    if guesses[question_num] == answer[question_num]:
        print("Your answer was correct")
        score += 1
    else:
        print("Incorrect")

    question_num += 1

print("__________________ Result ____________________")
print("Your guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print("Write Answer:", end=" ")
for writeanswer in answer:
    print(writeanswer, end=" ")
print()
score = score/len(questions)*100
print(f"Your score is {score}")
