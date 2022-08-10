
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import string

# Declearing constant variable arrays
numbers = string.digits  # range(10)
characters_lower = string.ascii_lowercase
characters_upper = string.ascii_uppercase
characters_special = string.punctuation


class PasswordGenerator:
    def generatePassword(self, length, indexes):
        print("\nGenerating password...")
        password = []

        while (True):
            # Randomize character type t
            t = random.randint(0, length - 1)

            # Break loop if ready
            if len(password) == length:
                # Check current password
                #checkPassword(password, indexed)
                return(password)

            # Generate lowercase character
            if t == 0 and (indexes.getLower(self) in range(1, 3)):
                password.append(characters_lower[random.randint(0, len(characters_lower) - 1)])
                print('Lowercase character')
                if (indexes.getLower(self) == 1):
                    indexes.setLower(2)

            # Generate uppercase character
            elif t == 1 and (indexes.getUpper(self) in range(1, 3)):
                password.append(characters_upper[random.randint(0, len(characters_upper) - 1)])
                print('Uppercase character')
                if (indexes.getUpper(self) == 1):
                    indexes.setUpper(2)

            # Generate number
            elif t == 2 and (indexes.getNumber(self) in range(1, 3)):
                password.append(numbers[random.randint(0, len(numbers) - 1)])
                print('Number')
                if (indexes.getNumber(self) == 1):
                    indexes.setNumber(2)

            # Generate special character
            elif t == 3 and (indexes.getSpecial(self) in range(1, 3)):
                password.append(characters_special[random.randint(0, len(characters_special) - 1)])
                print('Special character')
                if (indexes.getSpecial(self) == 1):
                    indexes.setSpecial(2)

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

        #password.printPassword(password)
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
            emptystr += i +''

        #ent_password.insert(0, f'{emptystr}')

# PASSWORDFRAME for password lenght and result
class PasswordFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        # field options
        options = {'padx': 5, 'pady': 0}

        # temperature label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w',  **options)

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
        self.temperature_entry.focus()

        # button
        self.generate_button = ttk.Button(self, text='\N{RIGHTWARDS BLACK ARROW}')
        self.generate_button.grid(column=2, row=0, sticky='w', **options)
        self.generate_button.configure(command=self.generate)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def generate(self):
        print("\nGenerating password...") #debug
        """  Handle button click event
        """
        try:
            # Get options
            input_value = float(self.temperature.get())
            #indexArr = [] [lower, upper, number, special] Meanings: 0=not required, 1=required, 2=included

            # Error handling
            if (input_value < 4):
                print(f'Password length is too short. Please, try again...')
                showerror(title='Error', message='Password length is too short. Please, try again...')

            elif Indexes.getLower(self) == 0:
                print(f'This password is not possible. Please, try again... :)))')
                showerror(title='Error', message='This password is not possible. Please, try again... :)))')

            else:
                result = PasswordGenerator.generatePassword(self, input_value, Indexes)
                self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''

