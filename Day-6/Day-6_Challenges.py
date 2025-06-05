#- Generate a random 8-character password
import random
import string

password=[
    random.choice(string.ascii_lowercase),  # Random letter (uppercase or lowercase)
    random.choice(string.ascii_uppercase),  # Random letter (uppercase)
    random.choice(string.digits),           # Random digit
    random.choice(string.punctuation),      # Random special character
]
password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=4)  # Add 4 more random characters
random.shuffle(password)  # Shuffle the characters to ensure randomness
redy_password = ''.join(password)  # Join the list into a string
password = redy_password
print("Generated Password:", password)