import argparse
import random
import string
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--exclude_numbers", action="store_true",
                    help="Exclude Numbers")
parser.add_argument("-ll", "--exclude_lletters", action="store_true",
                    help="Exclude Lowercase Letters")
parser.add_argument("-ul", "--exclude_uletters", action="store_true",
                    help="Exclude Uppercase Letters")
parser.add_argument("-sc", "--exclude_scharacters", action="store_true",
                    help="Exclude Special Characters")
args = parser.parse_args()

class Generating:
    def __init__(self, digits, ascii_lowercase, ascii_uppercase, punctuation):
        self.digits = digits
        self.ascii_lowercase = ascii_lowercase
        self.ascii_uppercase = ascii_uppercase
        self.punctuation = punctuation
        self.choices = [digits, ascii_lowercase, ascii_uppercase, punctuation]

    def numbers_arg(self):
        """Excludes Numbers if Argument was used."""
        if args.exclude_numbers:
            self.choices.remove(self.digits)

    def lowercase_letters_arg(self):
        """Excludes Lowercase Letters if Argument was used."""
        if args.exclude_lletters:
            self.choices.remove(self.ascii_lowercase)

    def uppercase_letters_arg(self):
        """Excludes Uppercase Letters if Argument was used."""
        if args.exclude_uletters:
            self.choices.remove(self.ascii_uppercase)

    def special_characters_arg(self):
        """Excludes Special Characters if Argument was used."""
        if args.exclude_scharacters:
            self.choices.remove(self.punctuation)

    def generate_password(self):
        if len(self.choices) == 0: # Check if every item in 'choices' list is excluded.
            sys.exit(0)

        try:
            password_length = int(input("Enter password length (Max. 256): "))
            if password_length > 256:
                print("Password is too long!")
                sys.exit(0)
        except ValueError:
            print("Wrong value, try again!")
            sys.exit(0)

        print("Generated Password: ", end="")
        for _ in range(password_length):
            print(random.choice(random.choice(self.choices)), end="")


p1 = Generating(string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
p1.numbers_arg()
p1.lowercase_letters_arg()
p1.uppercase_letters_arg()
p1.special_characters_arg()
p1.generate_password()
