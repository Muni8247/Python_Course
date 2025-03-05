import random

print("Welcome to my world, here you can create your password as per which type you want!!!")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "`", "~"]

numbers_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

alphabet = int(input("Enter the number of alphabets you want in the password: "))
char_list = int(input("Enter the number of special characters you want in the password: "))
numbers = int(input("Enter the number of numbers you want in the password: "))

password_list = []

# Add random letters
for i in range(1, alphabet + 1):
    char = random.choice(letters)
    password_list += char

# Add random special characters
for i in range(1, char_list + 1):
    char = random.choice(symbols)
    password_list += char

# Add random numbers
for i in range(1, numbers + 1):
    char = random.choice(numbers_n)
    password_list += str(char)  # Convert numbers to string for concatenation

print(password_list)
random.shuffle(password_list)
print(password_list)


passowrd=""
for mn in password_list:
    passowrd+=mn

print(passowrd)
