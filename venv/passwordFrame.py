
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import string
import optionsFrame
import optionsBackEnd


# PASSWORDFRAME for password lenght and result
class PasswordFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter, opt):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter
        self.opt = opt

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
            self.opt.lenght = int(self.temperature.get())
            print(f'Lenght is {self.opt.lenght}') # debug

            print(f'LOWER: {self.opt.lower}') # debug

            print(f'UPPER: {self.opt.upper}')  # debug

            print(f'NUMBER: {self.opt.number}')  # debug

            print(f'SPECIAL: {self.opt.special}')  # debug

            # Error handling
            if (self.opt.lenght < 4):
                print(f'Password length is too short. Please, try again...')
                showerror(title='Error', message='Password length is too short. Please, try again...')

            elif self.opt.lower != 1:
                print(f'This password is not possible. Please, try again... :)))')
                showerror(title='Error', message='This password is not possible. Please, try again... :)))')

            else:
                result = PasswordGenerator.generatePassword(self)
                self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''

# eof