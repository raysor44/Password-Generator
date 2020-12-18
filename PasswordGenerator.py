import argparse
import random
import string
import sys

from termcolor import colored
from colorama import init 


##################################

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--exclude_numbers", action="store_true", help="Exclude Numbers")
parser.add_argument("-ll", "--exclude_lletters", action="store_true", help="Exclude Lowercase Letters")
parser.add_argument("-ul", "--exclude_uletters", action="store_true", help="Exclude Uppercase Letters")
parser.add_argument("-sc", "--exclude_scharacters", action="store_true", help="Exclude Special Characters")
args = parser.parse_args()

##################################


def askForPasswordLength():
    global passwordLength

    try:
        passwordLength = int(input("How much characters you want to be in your password: "))
    except ValueError:
        print("Invalid Value, try again"); sys.exit(0)


class Generating:
    def randomNumbers(self):
        global usedNumbers
        usedNumbers = str(random.randint(0, 1000 * 1000))

        if args.exclude_numbers:
            print("\nUsed Numbers:", colored("None (Disabled)", "red"))
        else: 
            print("\nUsed Numbers:", colored(usedNumbers, "yellow"))

    def randomLowercaseLetters(self):
        global usedLowercaseLetters
        usedLowercaseLetters = string.ascii_lowercase

        if args.exclude_lletters:
            print("Used Lowercase Letters:", colored("None (Disabled)", "red"))
        else:
            print("Used Lowercase Letters:", colored(usedLowercaseLetters, "yellow"))
        
    def randomUppercaseLetters(self):
        global usedUppercaseLetters
        usedUppercaseLetters = string.ascii_uppercase

        if args.exclude_uletters:
            print("Used Uppercase Letters:", colored("None (Disabled)", "red"))
        else:
            print("Used Uppercase Letters:", colored(usedUppercaseLetters, "yellow"))

    def randomSpecialCharacters(self):
        global usedSpecialCharacters
        usedSpecialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*"]        

        if args.exclude_scharacters:
            print("Used Special Characters:", colored("None (Disabled)", "red"))
        else:
            print("Used Special Characters:", colored(usedSpecialCharacters, "yellow"))


    def generatePassword(self):
        choices = [usedNumbers, usedLowercaseLetters, usedUppercaseLetters, usedSpecialCharacters]

        if args.exclude_numbers:
            choices.remove(usedNumbers)
        
        if args.exclude_lletters:
            choices.remove(usedLowercaseLetters)
            
        if args.exclude_uletters:
            choices.remove(usedUppercaseLetters)
        
        if args.exclude_scharacters:
            choices.remove(usedSpecialCharacters)

        if len(choices) == 0: # Check if every item in 'choices' list is excluded.
            print("Password will not be generated"); sys.exit(0)

        print("Generated Password:", end=" ")

        for i in range(passwordLength):
            print(random.choice(random.choice(choices)), end="")


init() # Initialisation of Colorama Module
askForPasswordLength()

p1 = Generating()
p1.randomNumbers()
p1.randomLowercaseLetters()
p1.randomUppercaseLetters()
p1.randomSpecialCharacters()
p1.generatePassword()
