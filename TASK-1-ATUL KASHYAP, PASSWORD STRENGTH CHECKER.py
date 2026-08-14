import string

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = any(char.isupper() for char in password)
number = any(char.isdigit() for char in password)
symbol = any(char in string.punctuation for char in password)

score = 0

if length:
    score += 1

if uppercase:
    score += 1

if number:
    score += 1

if symbol:
    score += 1

if score <= 2:
    print("Password Strength : Weak")

elif score == 3:
    print("Password Strength : Medium")

else:
    print("Password Strength : Strong")
