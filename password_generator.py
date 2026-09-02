import random

print("Welcome to the password generator!")

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols= ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

combination= letters + numbers + symbols

user_letters= int(input('How many letters would you like in your password?'))
user_numbers= int(input('How many numbers would you like in your password?'))
user_symbols= int(input('How many symbols would you like in your password?'))

password=''

total = user_letters + user_numbers + user_symbols

for i in range(0,total):
    password += random.choice(combination)

print(f'Your password is: {password}')