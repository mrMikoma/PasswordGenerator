
import os
import json


# Constant variables
settingsPath = os.getcwd() + "\\venv\\"
settingsFile = "settings.json"


# Creates JSON if doesn't exists
def createJSON():
    if os.path.exists(settingsFile):
        print("File exists.")
        return

    # Else file not exists
    print("File doesn't exists.")

    # Default settings in dictionary
    defaultSettings = {
        "lower": 1,
        "upper": 1,
        "number": 1,
        "special": 0
    }

    # Create new file with default settings
    saveSettings(defaultSettings)
    return


# Reads setting from JSON file
def readSettings():
    # Opening JSON file
    with open(settingsPath + settingsFile, 'r') as openfile:
        # Reading from json file
        settings = json.load(openfile)

    return settings


# Saves settings into JSON file
def saveSettings(settings):
    # Serializing json
    json_object = json.dumps(settings, indent=4)
    print(settingsPath + settingsFile)
    # Writing to sample.json
    with open(os.getcwd() + "\\venv\\" + settingsFile, "w") as outfile:
        outfile.write(json_object)

    print("Settings saved successfully!")
    return

# eof