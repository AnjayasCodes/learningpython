foods = []
prices = []
while True:
    food = input(("Enter the name of the food (q to quit)"))
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food in $: $"))
        foods.append(food)
        prices.append(price)

print("--- Shopping Cart ---")
foods.sort()
for food in foods:
    print(food, end=" ")

print()
total = 0
for price in prices:
    total += price

print(f"The total cost of your shopping is ${total}")
