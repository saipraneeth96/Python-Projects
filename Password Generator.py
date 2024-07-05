# Password Generator

# LEVEL: EASY
"""
OUTPUT:
  Welcome to the Password Grnerator
  How many letters would you like to have in your Password
  6
  How many symbols would you like to have in your Password
  1
  How many numbers would you like to have in your Password
  2
  nsmgrp*57 (assumed expectation)
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '`', '[', ']', '{', '}', '|', ';',
           ':', ',', '<', '.', '>',
           '/', '?']

# LEVEL: EASY

print(" Welcome to the Password Generator, EASY \n")
n_letters = int(input("How many letters would you like to have in your Password? \n"))
n_symbols = int(input("How many symbols would you like to have in your Password? \n"))
n_numbers = int(input("How many numbers would you like to have in your Password? \n"))

password = " "

for i in range(0, n_letters + 1):
    char = random.choice(letters)
    password += char

for i in range(0, n_symbols + 1):
    char = random.choice(symbols)
    password += char

for i in range(0, n_numbers + 1):
    char = random.choice(numbers)
    password += char

print(f"The password is: {password}")

# LEVEL: HARD

print(" Welcome to the Password Generator, HARD \n")
n_letters = int(input("How many letters would you like to have in your Password? \n"))
n_symbols = int(input("How many symbols would you like to have in your Password? \n"))
n_numbers = int(input("How many numbers would you like to have in your Password? \n"))

password_list = []

for i in range(0, n_letters + 1):
    char = random.choice(letters)
    password_list += char

for i in range(0, n_symbols + 1):
    char = random.choice(symbols)
    password_list += char

for i in range(0, n_numbers + 1):
    char = random.choice(numbers)
    password_list += char

print(f"The password is: {password_list}")
random.shuffle(password_list)
print(f"The shuffled password is: {password_list}")

modified_password = " "
for char in password_list:
    modified_password += char

print(f"The modified password is: {modified_password}")
