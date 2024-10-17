import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomized
password_easy = []
password_easy += [random.choice(letters) for _ in range(nr_letters)]
password_easy += [random.choice(symbols) for _ in range(nr_symbols)]
password_easy += [random.choice(numbers) for _ in range(nr_numbers)]

# Convert the list into a string
easy_password = ''.join(password_easy)
print(f"Easy Level Password: {easy_password}")

# Hard Level - Order of characters randomized
password_hard = password_easy[:]  # Copy the password list
random.shuffle(password_hard)  # Shuffle the order of characters

# Convert the list into a string
hard_password = ''.join(password_hard)
print(f"Hard Level Password: {hard_password}")
