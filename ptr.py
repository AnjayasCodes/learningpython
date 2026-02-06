principle = 0
rate = 0
time = 0

while principle <= 0:
    print("principle can't be 0")
    principle = int(input("Enter the amount of principle"))

while time <= 0:
    print("Time can't be 0")
    time = int(input("Enter the amount of time"))

while rate <= 0:
    print("Rate can't be 0")
    rate = int(input("Enter the amount of rate"))

print(principle)
print(time)
print(rate)

print(f"The interest of the investment is {pow(principle*(1+rate/100), time)}")
