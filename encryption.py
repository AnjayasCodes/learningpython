import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

# print(chars)
# print(keys)

# Encryption
messaage = input("Enter the text you want to encrypt")
encrypted_text = ""

random.shuffle(keys)

for letter in messaage:
    index = chars.index(letter)
    encrypted_text += keys[index]

print(f"Encrypted text = {encrypted_text}")


# DeEncryption
messaage = input("Enter the text you want to deencrypt")
deencrypted_text = ""

for letter in messaage:
    index = keys.index(letter)
    deencrypted_text += chars[index]

print(f"DeEncrypted text = {deencrypted_text}")
