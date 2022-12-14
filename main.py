# This is a simple Python script for generating randomised passwords
# compiled by mrMikoma

# Thanks to
# - https://www.pythontutorial.net/tkinter/tkraise/
# - https://realpython.com/python-gui-tkinter/
# - https://realpython.com/courses/python-data-classes/

# PS. Cluster ry color: #d4202c

import tkinter as tk
from frontEnd import OptionsFrame

"""
Improvement ideas:
- :)
-
"""

# APPLICATION
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f'Password Generator')
        self.geometry('355x165')
        self.resizable(False, False)

# MAIN
if __name__ == '__main__':
    # Starting program
    print(f'\nHi, this is a really simple application for generating random password.\n')

    # Running program
    app = App()
    OptionsFrame(app)
    app.mainloop()

    # Ending program
    print(f'\nThank you for using this program! :)')

# eof