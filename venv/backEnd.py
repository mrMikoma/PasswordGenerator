
import random
import string
import frontEnd
import settings


# Declearing constant variable arrays for different characters
numbers = string.digits  # range(10)
characters_lower = string.ascii_lowercase
characters_upper = string.ascii_uppercase
characters_special = string.punctuation


def generatePassword(optDict, lenght):
    print("\nGenerating password...")
    password = []

    while True:
        # Randomize character type t
        t = random.randint(0, lenght - 1)

        # Break loop if ready
        if len(password) == lenght:
            # Check current password
            password = checkPassword(password, optDict, lenght)
            return ''.join(password)

        # Generate lowercase character
        if t == 0 and (optDict['lower'] in range(1, 3)):
            password.append(characters_lower[random.randint(0, len(characters_lower) - 1)])
            print('Lowercase character')
            if (optDict['lower'] == 1):
                optDict['lower'] = 2

        # Generate uppercase character
        elif t == 1 and (optDict['upper'] in range(1, 3)):
            password.append(characters_upper[random.randint(0, len(characters_upper) - 1)])
            print('Uppercase character')
            if (optDict['upper'] == 1):
                optDict['upper'] = 2

        # Generate number
        elif t == 2 and (optDict['number'] in range(1, 3)):
            password.append(numbers[random.randint(0, len(numbers) - 1)])
            print('Number')
            if (optDict['number'] == 1):
                optDict['number'] = 2

        # Generate special character
        elif t == 3 and (optDict['special'] in range(1, 3)):
            password.append(characters_special[random.randint(0, len(characters_special) - 1)])
            print('Special character')
            if (optDict['special'] == 1):
                optDict['special'] = 2

    return 'Error! :)'

def checkPassword(password, optDict, lenght):
    print(f'\nChecking password:')

    # Fail-safe for including all asked character types
    usedIndexes = []                                        # ADD THIS IN USE

    # Check and fix lowercase characters
    if (optDict['lower'] == 0):
        print(f'Lowercase characters not used.')

    elif (optDict['lower'] == 1):
        i = random.randint(0, len(password) - 1)
        password.pop(i)
        password.insert(i, characters_lower[random.randint(0, len(characters_lower) - 1)])
        print(f'Lowercase character fixed in index: {i}')

    else:
        print('Lowercase characters are ok.')

    # Check and fix uppercase characters
    if (optDict['upper'] == 0):
        print(f'Uppercase characters not used.')

    elif (optDict['upper'] == 1):
        i = random.randint(0, len(password) - 1)
        password.pop(i)
        password.insert(i, characters_upper[random.randint(0, len(characters_upper) - 1)])
        print(f'Uppercase character fixed in index: {i}')

    else:
        print('Uppercase characters are ok.')

    # Check and fix number characters
    if (optDict['number'] == 0):
        print(f'Numbers not used.')

    elif (optDict['number'] == 1):
        i = random.randint(0, len(password) - 1)
        password.pop(i)
        password.insert(i, numbers[random.randint(0, len(characters_upper) - 1)])
        print(f'Number character fixed in index: {i}')

    else:
        print('Number characters are ok.')

    # Check and fix special characters
    if (optDict['special'] == 0):
        print(f'Special characters not used.')

    elif (optDict['special'] == 1):
        i = random.randint(0, len(password) - 1)
        password.pop(i)
        password.insert(i, characters_special[random.randint(0, len(characters_upper) - 1)])
        print(f'Special character fixed in index: {i}')

    else:
        print('Special characters are ok.')

    print(f'\nPassword is now ok.')
    return password

# eof