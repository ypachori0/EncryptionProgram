# main.py
import random
import string
import sys
import os

# load in characters that will be used
chars = " " + string.punctuation + string.digits + string.ascii_letters

# turn the string into a list where each character is an individual element
chars = list(chars)
key = chars.copy()

# shuffle the key
random.shuffle(key)

# create the file that will hold encrypted messages
file_name = "cipher_texts.txt"
with open(file_name, 'w') as file:
    file.write("Encrypted texts:\n")
    file.write("\n")

while True:
    # MENU SYSTEM
    print("\n")
    print("----- WELCOME TO THE ENCRYPTION PROGRAM -----")
    print("Menu Options:")
    print("1: Encrypt text")
    print("2: Decrypt text")
    print("3: View encrypted texts")
    print("4: View list of characters")
    print("5: View key")
    print("6: Exit")

    # prompt user for input
    str = input("Please enter your choice (1-6): ")

    # main program
    if str == "1":
        #ENCRYPT
        # ask for user input
        plain_text = input("Enter a message to encrypt: ") # message to be encrypted
        cipher_text = "" # encrypted text

        # iterate over every letter in plain text
        for letter in plain_text:
            i = chars.index(letter)
            cipher_text += key[i]

        # return cipher text
        print(f"Original message: {plain_text}")
        print(f"Encrypted message: {cipher_text}")


        # ask user if they want to save message
        save_choice = input("Do you want to save your encrypted message? (y/n) ")
        if save_choice.lower() == "y":
            # add the encrypted message to the file
            with open(file_name, 'a') as file:
                file.write(cipher_text)
                file.write("\n")
        else:
            print("The encrypted message was not saved")

    elif str == "2":
        #DECRYPT
        # ask for user input
        cipher_text = input("Enter a message to decrypt: ") # message to be decrypted
        plain_text = " " # decrypted message

        # iterate over every letter in cipher text
        for letter in cipher_text:
            i = key.index(letter)
            plain_text += chars[i]

        # return plain text
        print(f"Original message: {cipher_text}")
        print(f"Decrypted message: {plain_text}")

    elif str == "3":
        print("\n")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

    elif str == "4":
        print(f"chars: {chars}")

    elif str == "5":
        print(f"key: {key}")

    elif str == "6":
        print("Deleting encrypted messages...")
        os.remove(file_name)
        print("Done")
        print("Exiting...")
        sys.exit()

    else:
        print("Error: Invalid input. Please try again.")