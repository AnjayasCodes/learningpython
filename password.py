password = input("Set a password")
if len(password) < 8:
    print("The password must be moer than 8 digit")

password_upper = False
password_number = False

for char in password:
    if char.isdigit():
        password_number = True

for char in password:
    if char.isupper():
        password_upper = True

if len(password) > 8 and password_upper and password_number:
    print("Strong password")
else:
    print("Weak password")
