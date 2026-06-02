from importlib.metadata import files
import os
import re
import unicodedata
from gui import GUI

# Set the directory to the folder you want to normalize.
directory = r"C:\Users\joona\Desktop\development\koekelberg\Sprites\badfiles"

def main():
    dir_path = directory
    gui = GUI(files, dir_path)
    gui.run()

main()