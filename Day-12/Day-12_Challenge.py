#- Validate gmail addresses using regex

import re

def check_gmail(email):
    pattern = r'^[a-zA-Z0-9](\.?[a-zA-Z0-9_-])*@gmail\.com$'
    
    if re.match(pattern, email):
        print(f"{email} is a valid Gmail address")
    else:
        print(f"{email} is not a valid Gmail address")

# Test the function with some email addresses
emails = [
    "nirbhay123@gmail.com",
    "nir.bhay.kumar@gmail.com",
    "nirbhay.@gmail.com",
    ".nirbhay@gmail.com",
    "nirbhay@outlook.com"
]

for e in emails:
    check_gmail(e)
# The function check_gmail checks if the provided email address is a valid Gmail address.