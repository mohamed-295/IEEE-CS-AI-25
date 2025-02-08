#Problem 6
import random
import string
def generate_password(length):
    characters = string.digits+string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password(8))
