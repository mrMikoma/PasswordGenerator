
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import string
import passwordFrame
import optionsBackEnd
from dataclasses import replace


# OPTIONSFRAME for different options
class OptionsFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'

        # Initializing options
        self.opt = optionsBackEnd.Options(0, 0, 0, 0, 0) #(lenght, lower, upper, number, special)

        # Initializing check buttons
        self.selected_lower = tk.IntVar()
        self.selected_upper = tk.IntVar()
        self.selected_number = tk.IntVar()
        self.selected_special = tk.IntVar()

        cbtn_lower = tk.Checkbutton(
            self,
            text='Lowercase',
            variable=self.selected_lower,
            command=print(f'Lower is set to {self.selected_lower.get()}'))\
            .grid(column=0, row=0, padx=5, pady=5)

        cbtn_upper = tk.Checkbutton(
            self,
            text='Uppercase',
            variable=self.selected_upper,
            command=print(f'Upper is set to {self.selected_upper.get()}'))\
            .grid(column=1, row=0, padx=5, pady=5)

        cbtn_number = tk.Checkbutton(
            self,
            text='Number',
            variable=self.selected_number,
            command=print(f'Number is set to {self.selected_number.get()}'))\
            .grid(column=2, row=0, padx=5, pady=5)

        cbtn_special = tk.Checkbutton(
            self,
            text='Special',
            variable=self.selected_special,
            command=print(f'Special is set to {self.selected_special.get()}'))\
            .grid(column=3, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # Initialize frames
        self.frames = {}
        self.save_options() # FOR SAVING OPTIONS
        self.frames[0] = passwordFrame.PasswordFrame(
            container,
            'Password lenght',
            passwordFrame.PasswordFrame.generate,
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


# eof