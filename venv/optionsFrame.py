
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import string
from passwordFrame import PasswordFrame

# INDEXES for different options
class Indexes():
  def __init__(self, lower, upper, number, special):
    self.lower = lower
    self.upper = upper
    self.number = number
    self.special = special

  def setLower(self, newValue):
    self.lower = newValue
    print(f'Lowercase value changed to {self.lower}')

  def getLower(self):
    print(f'Lowercase value was {self.lower}')
    return(self.lower)

  def setUpper(self, newValue):
    self.upper = newValue
    print(f'Uppercase value changed to {self.upper}')

  def getUpper(self):
    print(f'Uppercase value was {self.upper}')
    return(self.upper)

  def setNumber(self, newValue):
    self.number = newValue
    print(f'Number value changed to {self.number}')

  def getNumber(self):
    print(f'Number value was {self.number}')
    return(self.number)

  def setSpecial(self, newValue):
    self.special = newValue
    print(f'Special value changed to {self.special}')

  def getSpecial(self):
    print(f'Special value was {self.special}')
    return(self.special)



# OPTIONSFRAME for different options
class OptionsFrame(ttk.LabelFrame):
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
            command=Indexes.setLower(self, self.selected_lower.get()))\
            .grid(column=0, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Uppercase',
            variable=self.selected_upper,
            command=Indexes.setUpper(self, self.selected_upper.get()))\
            .grid(column=1, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Number',
            variable=self.selected_number,
            command=Indexes.setNumber(self, self.selected_number.get()))\
            .grid(column=2, row=0, padx=5, pady=5)

        tk.Checkbutton(
            self,
            text='Special',
            variable=self.selected_special,
            command=Indexes.setSpecial(self, self.selected_special.get()))\
            .grid(column=3, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # Initialize options
        #indexes = Indexes(self.selected_lower.get(), self.selected_upper.get(), self.selected_number.get(), self.selected_special.get())
        #indexes.setLower(self, self.selected_lower.get())
        #indexes.setUpper(self, self.selected_upper.get())
        #indexes.setNumber(self, self.selected_number.get())
        #indexes.setSpecial(self, self.selected_special.get())

        # Initialize frames
        self.frames = {}
        self.frames[0] = PasswordFrame(container, 'Password lenght', PasswordFrame.generate)

        #self.frames[1] = ConverterFrame(
        #    container,
        #    'Celsius',
        #    TemperatureConverter.celsius_to_fahrenheit)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[0]
        frame.reset()
        frame.tkraise()

