import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    "|",
    ";",
    ":",
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
    "~",
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to password generator!!")

r_letters = int(input("how many letters would you like in your password? \n"))
r_numbers = int(input("how many number would you like \n"))
r_symbols = int(input("how many symbols would you like \n"))

print(r_letters, r_numbers, r_symbols)
password = ""

for item in range(0, r_letters):
    password = password + letters[random.randint(0, len(letters))]
for item in range(0, r_numbers):
    password = password + str(numbers[random.randint(0, len(numbers))])
for item in range(0, r_symbols):
    password = password + symbols[random.randint(0, len(numbers))]
    
    
print(password)    
