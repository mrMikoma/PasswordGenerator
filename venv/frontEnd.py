
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import string
import backEnd
import settings

# OPTIONSFRAME for different options
class OptionsFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'

        # Get saved options from settings file
        opt = settings.readSettings()

        # Initializing check button variables
        self.selected_lower = tk.IntVar()
        self.selected_upper = tk.IntVar()
        self.selected_number = tk.IntVar()
        self.selected_special = tk.IntVar()

        cbtn_lower = tk.Checkbutton(
            self,
            text='Lowercase',
            variable=self.selected_lower,
            command=lambda: print(f'Lower is set to {self.selected_lower.get()}'))\
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

        # Save button for options
        self.save_button = ttk.Button(self, text='Save')
        self.save_button.grid(column=0, row=1, sticky='ew')
        self.save_button.configure(command= lambda: self.save_options() )

        # Initialize correct options
        self.selected_lower.set(opt['lower'])
        self.selected_upper.set(opt['upper'])
        self.selected_number.set(opt['number'])
        self.selected_special.set(opt['special'])

        # Initialize frames
        self.frames = {}
        self.frames[0] = PasswordFrame(
            container,
            'Password lenght',
            PasswordFrame.generate
            )

        self.change_frame()

    def change_frame(self):
        frame = self.frames[0]
        frame.reset()
        frame.tkraise()

    def save_options(self):
        # Declaring new settings
        new_opt = {
            "lower": self.selected_lower.get(),
            "upper": self.selected_upper.get(),
            "number": self.selected_number.get(),
            "special": self.selected_special.get()
            }

        # Saving new settings
        settings.saveSettings(new_opt)

        #self.change_frame()

        print(f'\nOptions saved successfully!\n')



# PASSWORDFRAME for password lenght and result
class PasswordFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        # field options
        options = {'padx': 5, 'pady': 0}

        # lenght label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w',  **options)

        # lenght entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=0, row=1, sticky='w', **options)
        self.temperature_entry.focus()

        # generate_button
        self.generate_button = ttk.Button(self, text='\N{RIGHTWARDS BLACK ARROW}')
        self.generate_button.grid(column=1, row=1, sticky='w', **options)
        self.generate_button.configure(command= lambda: self.generate() )

        # result_entry
        self.result_entry = tk.Entry(self, width=36)
        self.eText = tk.StringVar()
        self.result_entry.grid(column=0, row=2, sticky='w', **options) # row=1, columnspan=2, **options
        self.result_entry.configure(state="readonly", textvariable=self.eText)

        # clipboard copy_button
        self.copy_button = ttk.Button(self, text='Copy')
        self.copy_button.grid(column=1, row=2, sticky='w', **options)
        self.copy_button.configure(command=lambda: self.copyClipboard())

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def generate(self):
        print("\nGenerating password...") #debug

        # Check options
        try:
            # Get password lenght
            lenght = int(self.temperature.get())

            # Get character options
            opt = settings.readSettings()
            print(opt)      # debug

            # Error handling for too short password
            if lenght < 4:
                print(f'Password length is too short. Please, try again...')
                showerror(title='Error', message='Password length is too short. Please, try again...')
                return

            # Error handling for not suitable character options
            elif opt['lower'] == 0 and opt['upper'] == 0 and opt['number'] == 0 and opt['special'] == 0:
                print(f'This password is not possible. Please, try again...')
                showerror(title='Error', message='This password is not possible. Please, try again...')
                return

            else:
                result = backEnd.generatePassword(opt, lenght)
                self.eText.set(result)

        except ValueError as error:
            showerror(title='Error', message=error)

    def copyClipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.eText.get())

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_entry.insert(0, '')

# eof