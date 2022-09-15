
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import string
import backEnd
from dataclasses import replace


# OPTIONSFRAME for different options
class OptionsFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'

        # Initializing options
        self.opt = backEnd.Options(0, 0, 0, 0, 0) #(lenght, lower, upper, number, special)

        # Initializing check buttons
        self.selected_lower = tk.IntVar()
        self.selected_upper = tk.IntVar()
        self.selected_number = tk.IntVar()
        self.selected_special = tk.IntVar()

        cbtn_lower = tk.Checkbutton(
            self,
            text='Lowercase',
            variable=self.selected_lower,
            command=lambda: backEnd.replace(self.opt, lower=self.selected_lower.get()))\
            .grid(column=0, row=0, padx=5, pady=5)

        cbtn_upper = tk.Checkbutton(
            self,
            text='Uppercase',
            variable=self.selected_upper,
            command=lambda: print(f'Upper is set to {self.selected_upper.get()}'))\
            .grid(column=1, row=0, padx=5, pady=5)

        cbtn_number = tk.Checkbutton(
            self,
            text='Number',
            variable=self.selected_number,
            command=lambda: print(f'Number is set to {self.selected_number.get()}'))\
            .grid(column=2, row=0, padx=5, pady=5)

        cbtn_special = tk.Checkbutton(
            self,
            text='Special',
            variable=self.selected_special,
            command=lambda: print(f'Special is set to {self.selected_special.get()}'))\
            .grid(column=3, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # save_button
        self.save_button = ttk.Button(self, text='Save')
        self.save_button.grid(column=0, row=1, sticky='ew')
        self.save_button.configure(command= lambda: self.save_options() )

        # Initialize frames
        self.frames = {}
        self.frames[0] = PasswordFrame(
            container,
            'Password lenght',
            PasswordFrame.generate,
            self.opt )

        self.change_frame()

    def change_frame(self):
        frame = self.frames[0]
        frame.reset()
        frame.tkraise()

    def save_options(self):
        replace(self.opt, lower=self.selected_lower.get())
        replace(self.opt, upper=self.selected_upper.get())
        replace(self.opt, number=self.selected_number.get())
        replace(self.opt, special=self.selected_special.get())

        print(f'LoWer: {self.selected_lower.get()}') # debug
        print(f'\nOptions saved successfully!\n')



# PASSWORDFRAME for password lenght and result
class PasswordFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter, opt):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter
        self.opt = opt

        print(f'LÖÖVER: {self.opt.lower}')  # debug

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

        # generate_button
        self.generate_button = ttk.Button(self, text='\N{RIGHTWARDS BLACK ARROW}')
        self.generate_button.grid(column=2, row=0, sticky='w', **options)
        self.generate_button.configure(command=self.generate)

        # result_label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def generate(self):
        print("\nGenerating password...") #debug

        try:
            # Get options
            self.opt.lenght = int(self.temperature.get())





            print(f'Lenght is {self.opt.lower}') # debug

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