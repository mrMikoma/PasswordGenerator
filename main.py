# This is a simple Python script for generating random passwords
# made by mrMikoma

# PS. Cluster ry color: #d4202c

import tkinter as tk
from this import s
from tkinter import ttk
from tkinter.messagebox import showerror
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

# INDEXES for different options
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


class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f, format=True):
        result = (f - 32) * 5/9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result

    @staticmethod
    def celsius_to_fahrenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Fahrenheit'
        return result

class PasswordGenerator:
    def testPrint(name):
        print(f"Hi, it's running my friend {name}!\n")

    def generatePassword(length):
        print("\nGenerating password...")
        password = []

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
            return (0)

        while (True):
            # Randomize character type t
            t = random.randint(0, length - 1)

            # Break loop if ready
            if len(password) == length:
                # Check current password
                #checkPassword(password, indexed)
                return(password)

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

        ent_password.insert(0, f'{emptystr}')

# PASSWORDFRAME for password lenght and result
class ConverterFrame(ttk.Frame):
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

    def generate(self, event=None):
        print("\nGenerating password...") #debug
        """  Handle button click event
        """
        try:
            input_value = float(self.temperature.get())
            if (input_value < 4):
                print(f'Password length is too short. Please, try again...')
                showerror(title='Error', message='Password length is too short. Please, try again...')
            else:
                result = PasswordGenerator.generatePassword(input_value)
                self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''

# OPTIONSFRAME for different options
class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # check boxes
        self.selected_lower = tk.IntVar()
        self.selected_upper = tk.IntVar()
        self.selected_number = tk.IntVar()
        self.selected_special = tk.IntVar()

        tk.Checkbutton(
            self,
            text='Lowercase',
            variable=self.selected_lower,
            command=Indexes.setLower(self, self.selected_lower))\
            .grid(column=0, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Uppercase',
            variable=self.selected_upper,
            command=Indexes.setUpper(self, self.selected_upper))\
            .grid(column=1, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Number',
            variable=self.selected_number,
            command=Indexes.setNumber(self, self.selected_number))\
            .grid(column=2, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Special',
            variable=self.selected_special,
            command=Indexes.setSpecial(self, self.selected_special))\
            .grid(column=3, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(container, 'Password lenght', ConverterFrame.generate)

        #self.frames[1] = ConverterFrame(
        #    container,
        #    'Celsius',
        #    TemperatureConverter.celsius_to_fahrenheit)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[0]
        frame.reset()
        frame.tkraise()

# APPLICATION
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(f'Password Generator')
        self.geometry('350x120')
        self.resizable(False, False)

# MAIN
if __name__ == '__main__':
    # Starting program
    print(f'\nHi, this is a really simple application for generating random password.')

    # Running program
    app = App()
    ControlFrame(app)
    app.mainloop()

    # Ending program
    print(f'\n\nThank you for using this program! :)')

# EOF