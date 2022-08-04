# This is a simple Python script for generating random passwords
# made by mrMikoma

# PS. Cluster ry color: #d4202c

import tkinter as tk
import random
import string

"""
Improvement ideas:
- fixing indexing on 'fixing' the password
-
"""


# Declearing constant variable arrays
numbers = string.digits  # range(10)
characters_lower = string.ascii_lowercase
characters_upper = string.ascii_uppercase
characters_special = string.punctuation

class Indexes:
  def __init__(self, lower, upper, number, special):
    self.lower = lower
    self.upper = upper
    self.number = number
    self.special = special

  def setLower(self, newValue):
    self.lower = newValue
    print(f'Lowercase value changed to {self.lower}')

  def getLower(self):
    return(self.lower)

  def setUpper(self, newValue):
    self.upper = newValue
    print(f'Uppercase value changed to {self.upper}')

  def getUpper(self):
    return(self.upper)

  def setNumber(self, newValue):
    self.number = newValue
    print(f'Number value changed to {self.number}')

  def getNumber(self):
    return(self.number)

  def setSpecial(self, newValue):
    self.special = newValue
    print(f'Special value changed to {self.special}')

  def getSpecial(self):
    return(self.special)



def testPrint(name):
    print(f"Hi, it's running my friend {name}!\n")

def generatePassword():
    print("\nGenerating password...")
    password = []

    lenght = int(ent_length.get())

    indexArr = [0, 0, 0, 0]  # [lower, upper, number, special] Meanings: 0=not required, 1=required, 2=included
    # if (input(f'Lowercase characters (x): ') == 'x'):
    indexArr[0] = 1
    # if (input(f'Uppercase characters (x): ') == 'x'):
    indexArr[1] = 1
    # if (input(f'Number characters (x): ') == 'x'):
    indexArr[2] = 1
    # if (input(f'Special characters (x): ') == 'x'):
    indexArr[3] = 1
    # else:
    #    indexArr[3] = 0

    indexed = Indexes(indexArr[0], indexArr[1], indexArr[2], indexArr[3])

    while (True):
        # Randomize character type t
        t = random.randint(0, lenght - 1)

        # Break loop if ready
        if len(password) == lenght:
            # Check current password
            password = checkPassword(password, indexed)
            break

        # Generate lowercase character
        if t == 0 and (indexArr[0] in range(1, 3)):
            password.append(characters_lower[random.randint(0, len(characters_lower) - 1)])
            print('Lowercase character')
            if (indexed.getLower() == 1):
                indexed.setLower(2)

        # Generate uppercase character
        elif t == 1 and (indexArr[1] in range(1, 3)):
            password.append(characters_upper[random.randint(0, len(characters_upper) - 1)])
            print('Uppercase character')
            if (indexed.getUpper() == 1):
                indexed.setUpper(2)

        # Generate number
        elif t == 2 and (indexArr[2] in range(1, 3)):
            password.append(numbers[random.randint(0, len(numbers) - 1)])
            print('Number')
            if (indexed.getNumber() == 1):
                indexed.setNumber(2)

        # Generate special character
        elif t == 3 and (indexArr[3] in range(1, 3)):
            password.append(characters_special[random.randint(0, len(characters_special) - 1)])
            print('Special character')
            if (indexed.getSpecial() == 1):
                indexed.setSpecial(2)

    return (password)


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

    printPassword(password)

    return (0)

def printPassword(pw):
    print(f"\nAnd here is your password: ", end='')
    emptystr = ""
    for i in pw:
        print(i, end='')
        emptystr += i +''

    lbl_password["text"] = f"{emptystr}"

def print_hi():
    print(f'Hi, {ent_length.get()}')
    lbl_password["text"] = f"{ent_length.get()}"


# Main script
if __name__ == '__main__':
    # Set up the window
    window = tk.Tk()
    window.title("Password generator")
    window.resizable(width=False, height=False)

    # Create the length entry frame with an Entry
    # widget and label in it
    frm_entry = tk.Frame(master=window)
    lbl_title = tk.Label(master=frm_entry, text="Password generator")
    ent_length = tk.Entry(master=frm_entry, width=10)
    lbl_pw_length = tk.Label(master=frm_entry, text="Password length:")
    lbl_password = tk.Label(master=window, text="")

    # Layout the temperature Entry and Label in frm_entry
    # using the .grid() geometry manager
    lbl_title.grid(row=0, column=0, sticky="w")
    ent_length.grid(row=1, column=1, sticky="e")
    lbl_pw_length.grid(row=1, column=0, sticky="w")

    # Create the generate button
    btn_generate = tk.Button(
        master=window,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=generatePassword
    )

    # Set up the layout using the .grid() geometry manager
    frm_entry.grid(row=0, column=0, padx=10)
    btn_generate.grid(row=0, column=1, pady=10)
    lbl_password.grid(row=0, column=2, padx=10)

    # Run the application
    window.mainloop()

    # Test
    name = 'mrMikoma'
    testPrint(name)

    # VARIABLES
    length = 0
    while (True):
        try:
            length = int(input(f'Give password length: '))
            if (length < 4):
                print(f'Password length is too short. Please, try again...')
                continue
            break
        except ValueError:
            print("Could not convert data to an integer. Please, try again...")

    # Generating password
    while (True):
        indexArr = [0, 0, 0, 0]  # [lower, upper, number, special] Meanings: 0=not required, 1=required, 2=included
        # if (input(f'Lowercase characters (x): ') == 'x'):
        indexArr[0] = 1
        # if (input(f'Uppercase characters (x): ') == 'x'):
        indexArr[1] = 1
        # if (input(f'Number characters (x): ') == 'x'):
        indexArr[2] = 1
        # if (input(f'Special characters (x): ') == 'x'):
        indexArr[3] = 1
        # else:
        #    indexArr[3] = 0

        indexed = Indexes(indexArr[0], indexArr[1], indexArr[2], indexArr[3])

        if indexArr == [0, 0, 0, 0]:
            print(f'Your password is not possible! Please, try again...')

        else:
            password = generatePassword(length, indexed)
            break

    # Ending program
    printPassword(password)
    print(f'\n\nThank you for using this program! :)')


# EOF