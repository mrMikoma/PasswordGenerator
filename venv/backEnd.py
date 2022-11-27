
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
    lenght: int  = 16
    lower: int  = 1
    upper: int = 1
    number: int = 1
    special: int = 0


def generatePassword(opt):
    print("\nGenerating password...")
    password = []
    includeList = [opt.lower,
                   opt.upper,
                   opt.number,
                   opt.special]
    i = 0  # debug

    while True:
        # Randomize character type t
        t = random.randint(0, opt.lenght - 1)

        # Break loop if ready
        if len(password) == opt.lenght:
            # Check current password                # NOTICE and fix!
            # checkPassword(password, indexed)      # NOTICE and fix!
            return password

        # Generate lowercase character
        if t == 0 and (opt.lower in range(1, 3)):
            password.append(characters_lower[random.randint(0, len(characters_lower) - 1)])
            print('Lowercase character')
            if (opt.lenght == 1):
                includeList[0] = 2

        # Generate uppercase character
        elif t == 1 and (opt.upper in range(1, 3)):
            password.append(characters_upper[random.randint(0, len(characters_upper) - 1)])
            print('Uppercase character')
            if (opt.upper == 1):
                includeList[1] = 2

        # Generate number
        elif t == 2 and (opt.number in range(1, 3)):
            password.append(numbers[random.randint(0, len(numbers) - 1)])
            print('Number')
            if (opt.number == 1):
                includeList[2] = 2

        # Generate special character
        elif t == 3 and (opt.special in range(1, 3)):
            password.append(characters_special[random.randint(0, len(characters_special) - 1)])
            print('Special character')
            if (opt.special == 1):
                includeList[3] = 2
        """
        else:  # debug
            i += 1
            if (i >= 10):
                break
        """

    return 'Error! :)'

def checkPassword(self, password, indexes):
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
    psw_string = ''.join(password)
    print(f"\nAnd here is your password: {psw_string}")

    return (psw_string)


# eof