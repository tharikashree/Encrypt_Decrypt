import random
import string

chars= " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars:{chars}")
print(f"key:{key}")

#ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index] 

print(f"orginal message : {plain_text}")
print(f"encrypted message : {cipher_text}")
