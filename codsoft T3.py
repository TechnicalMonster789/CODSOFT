import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+"
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

try:
    user_length = int(input("Enter the desired length of the password: "))
    if user_length <= 0:
        print("Please enter a positive number.")
    else:
        generated_password = generate_password(user_length)
        if generated_password:
            print("Your generated password is:", generated_password)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
