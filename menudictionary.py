menu = {"Pizze": 1.99,
        "Popcorn": 2,
        "Sprite": 3,
        "Coke": 2,
        "Fries": 3
        }

cart = []
total = 0

print("___________MENU________________")
print()
for key, values in menu.items():
    print(f"{key:10}: ${values:.2f}")

print("_______________________________")

while True:
    food = input("Chosse the food you want to purchase(q to quit)")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)
print("--------------Cart---------------")
for food in cart:
    print(food, end=" ")
print()
print(f"Your total cost is {total}")
