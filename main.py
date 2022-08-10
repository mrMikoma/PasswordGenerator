# This is a simple Python script for generating random passwords
# compiled by mrMikoma

# Thanks to
# - https://www.pythontutorial.net/tkinter/tkraise/

# PS. Cluster ry color: #d4202c

import tkinter as tk
from optionsFrame import OptionsFrame

"""
Improvement ideas:
- FIX ALL :)
-
"""

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
    OptionsFrame(app)
    app.mainloop()

    # Ending program
    print(f'\n\nThank you for using this program! :)')

# EOF