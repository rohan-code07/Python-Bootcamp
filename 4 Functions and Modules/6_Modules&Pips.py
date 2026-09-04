# MODULES

# Two types of modules in python:
# -Built in Module
# -External Module

import math
print(math.sqrt(16))
print(math.factorial(5))


import datetime
print(datetime.datetime.now())     # tells the time and date

import random
print(random.randint(1,100))       # choose random int b/w 1 to 100

import sys
print(sys.version)                 # Used to interact with the system

import os
print(os.getcwd())                          # Returns the current working directory
print(os.listdir())                         # Shows all files and folders in the directory
print(os.mkdir("new_folder"))               # Create a new folder
print(os.rmdir("new_folder"))               # Remove a folder
print(os.path.exists("1_functions.py"))     # Check if File Exists
print(os.path.getsize("1_Functions.py"))    # Get file information


# Creating your owm module

import Mymodule
print(Mymodule.hello("Rohan"))
print(Mymodule.batsman("Virat Kohli"))
print(Mymodule.square(5))
print(Mymodule.cube(3))
print(Mymodule.is_even(4))

# PIP 

# Some modules are not included in Python, like:
# numpy (for calculations)
# pandas (for data handling)
# matplotlib (for graphs)
# To use them, we install using pip

# External module text to speak

import pyttsx3
engine = pyttsx3.init()

engine.say("Hello my name is rohan")
engine.runAndWait()

import requests

response = requests.get("https://api.github.com")
print(response.text)          # response.status_code
 