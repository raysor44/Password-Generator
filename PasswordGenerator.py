import random
import string

# This script automatically generates password of 15 characters length.

specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*"]

class Generating:
    def GenerateRandomNumbers(self):
        global generatedNumbers

        generatedNumbers = str(random.randint(0, 1000 * 1000))
        print("Generated Numbers:", generatedNumbers)

    def GenerateRandomLetters(self):
        global generatedLetters

        generatedLetters = string.ascii_letters
        print("Generated Letters:", generatedLetters)

    def GeneratePassword(self):
        result = "".join(random.choice(generatedNumbers) + random.choice(generatedLetters) + random.choice(specialCharacters) for i in range (0, 5))

        print("Generated Password:", result)


p1 = Generating()
p1.GenerateRandomNumbers()
p1.GenerateRandomLetters()
p1.GeneratePassword()
