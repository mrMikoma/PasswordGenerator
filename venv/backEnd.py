
import random
import string
import frontEnd
from dataclasses import dataclass
from dataclasses import replace


# Declearing constant variable arrays
numbers = string.digits  # range(10)
characters_lower = string.ascii_lowercase
characters_upper = string.ascii_uppercase
characters_special = string.punctuation



@dataclass
class Options:
    lenght: int = 0
    lower: int = 0
    upper: int = 0
    number: int = 0
    special: int = 0


class PasswordGenerator:
    def generatePassword(self):
        print("\nGenerating password...")
        password = []
        i = 0  # debug

        while (True):
            # Randomize character type t
            t = random.randint(0, self.lenght - 1)

            # Break loop if ready
            if len(password) == self.lenght:
                # Check current password
                # checkPassword(password, indexed)
                return (password)

            # Generate lowercase character
            if t == 0 and (self.indexes.getLower() in range(1, 3)):
                password.append(characters_lower[random.randint(0, len(characters_lower) - 1)])
                print('Lowercase character')
                if (self.indexes.getLower() == 1):
                    self.indexes.setLower(2)

            # Generate uppercase character
            elif t == 1 and (self.indexes.getUpper() in range(1, 3)):
                password.append(characters_upper[random.randint(0, len(characters_upper) - 1)])
                print('Uppercase character')
                if (self.indexes.getUpper() == 1):
                    self.indexes.setUpper(2)

            # Generate number
            elif t == 2 and (self.indexes.getNumber() in range(1, 3)):
                password.append(numbers[random.randint(0, len(numbers) - 1)])
                print('Number')
                if (self.indexes.getNumber() == 1):
                    self.indexes.setNumber(2)

            # Generate special character
            elif t == 3 and (self.indexes.getSpecial() in range(1, 3)):
                password.append(characters_special[random.randint(0, len(characters_special) - 1)])
                print('Special character')
                if (self.indexes.getSpecial() == 1):
                    self.indexes.setSpecial(2)

            else:  # debug
                i += 1
                if (i >= 10):
                    break

        return ('Error! :)')

    def checkPassword(password, indexes):
        print(f'\nChecking password:')

        usedIndexes = []  # ADD THIS IN USE

        # Check and fix lowercase characters
        if (indexes.getLower() == 0):
            print(f'Lowercase characters not used.')

        elif (indexes.getLower() == 1):
            i = random.randint(0, len(password) - 1)
            password.pop(i)
            password.insert(i, characters_lower[random.randint(0, len(characters_lower) - 1)])
            print(f'Lowercase character fixed for index: {i}')

        else:
            print('Lowercase characters are ok.')

        # Check and fix uppercase characters
        if (indexes.getUpper() == 0):
            print(f'Uppercase characters not used.')

        elif (indexes.getUpper() == 1):
            i = random.randint(0, len(password) - 1)
            password.pop(i)
            password.insert(i, characters_upper[random.randint(0, len(characters_upper) - 1)])
            print(f'Uppercase character fixed for index: {i}')

        else:
            print('Uppercase characters are ok.')

        # Check and fix number characters
        if (indexes.getNumber() == 0):
            print(f'Numbers not used.')

        elif (indexes.getNumber() == 1):
            i = random.randint(0, len(password) - 1)
            password.pop(i)
            password.insert(i, numbers[random.randint(0, len(characters_upper) - 1)])
            print(f'Number character fixed for index: {i}')

        else:
            print('Number characters are ok.')

        # Check and fix special characters
        if (indexes.getSpecial() == 0):
            print(f'Special characters not used.')

        if (indexes.getSpecial() == 1):
            i = random.randint(0, len(password) - 1)
            password.pop(i)
            password.insert(i, characters_special[random.randint(0, len(characters_upper) - 1)])
            print(f'Special character fixed for index: {i}')

        else:
            print('Special characters are ok.')

        print(f'Password is now ok.')

        # password.printPassword(password)
        emptystr = ""
        for i in password:
            print(i, end='')
            emptystr += i + ''

        return (emptystr)

    def printPassword(pw):
        print(f"\nAnd here is your password: ", end='')
        emptystr = ""
        for i in pw:
            print(i, end='')
            emptystr += i + ''

        # ent_password.insert(0, f'{emptystr}')

# eof