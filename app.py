from gui import GUI
import os
from dotenv import load_dotenv

load_dotenv()

DIRECTORY = os.getenv('FOLDER')

def main():
    gui = GUI(DIRECTORY)
    gui.run()

main()