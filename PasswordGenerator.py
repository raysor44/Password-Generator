import argparse
import random
import string
import sys

from termcolor import colored as col
from colorama import init 


def ask_for_password_length():
    global passwordLength

    try:
        passwordLength = int(input("How much characters you want to be in your password: "))
    except ValueError:
        print("Invalid Value, try again"); sys.exit(0)


class ArgumentParser:
    global args
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--exclude_numbers", action="store_true", help="Exclude Numbers")
    parser.add_argument("-ll", "--exclude_lletters", action="store_true", help="Exclude Lowercase Letters")
    parser.add_argument("-ul", "--exclude_uletters", action="store_true", help="Exclude Uppercase Letters")
    parser.add_argument("-sc", "--exclude_scharacters", action="store_true", help="Exclude Special Characters")
    args = parser.parse_args()


class Generating:
    def __init__(self, digits, ascii_lowercase, ascii_uppercase, punctuation):
        self.digits = digits
        self.ascii_lowercase = ascii_lowercase
        self.ascii_uppercase = ascii_uppercase
        self.punctuation = punctuation
        self.choices = [digits, ascii_lowercase, ascii_uppercase, punctuation]
    
    def random_numbers(self):
        if args.exclude_numbers:
            self.choices.remove(self.digits)
            
            print("Used Numbers:", col("None (Disabled)", "red"))
        else: 
            print("Used Numbers:", col(self.digits, "yellow"))

    def random_lowercase_letters(self):
        if args.exclude_lletters:
            self.choices.remove(self.ascii_lowercase)
            
            print("Used Lowercase Letters:", col("None (Disabled)", "red"))
        else: 
            print("Used Lowercase Letters:", col(self.ascii_lowercase, "yellow"))
            
    def random_uppercase_letters(self):
        if args.exclude_uletters:
            self.choices.remove(self.ascii_uppercase)
            
            print("Used Uppercase Letters:", col("None (Disabled)", "red"))
        else: 
            print("Used Uppercase Letters:", col(self.ascii_uppercase, "yellow"))

    def random_special_characters(self):
        if args.exclude_scharacters:
            self.choices.remove(self.punctuation)
            
            print("Used Special Characters:", col("None (Disabled)", "red"))
        else: 
            print("Used Special Characters:", col(self.punctuation, "yellow"))
            
    def generate_password(self):
        if len(self.choices) == 0: # Check if every item in 'choices' list is excluded.
            print("Password can't be generated"); sys.exit(0)

        print("Password Generator:", end=" ")

        for i in range(passwordLength):
            print(random.choice(random.choice(self.choices)), end="")


init() # Initialisation of Colorama Module
ask_for_password_length()

p1 = Generating(string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
p1.random_numbers()
p1.random_lowercase_letters()
p1.random_uppercase_letters()
p1.random_special_characters()
p1.generate_password()
