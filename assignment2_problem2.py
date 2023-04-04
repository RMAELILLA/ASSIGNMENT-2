# This program will decrypt user's encrypted input

# Ronio, Ryza Mae P
# BSCpE 1-4
# Assignment 2 Problem 2

# Let user input encrypted text
encrypt_input = input("Enter sentence you need to decrypt: ")
encrypted = ""
# Evaluate encrypted text
for i in range(len(encrypt_input)):
#   If input encrypted by * change a
    if encrypt_input[i] == "*" :
        encrypted += "a"
#   If input encrypted by & change e
    elif encrypt_input[i] == "&" :
        encrypted += "e"
#   If input encrypted by # change i
    elif encrypt_input[i] == "#" :
        encrypted += "i"
#   If input encrypted by + change o
    elif encrypt_input[i] == "+" :
        encrypted += "o"
#   If input encrypted by ! change u
    elif encrypt_input[i] == "!" :
        encrypted += "u"
    else:
        encrypted += encrypt_input[i]
# Display decryption
print('\033[1;35;47m◊' * 120)
encrypted
print(encrypted.center(120, "◊"))
print("◊" * 120)