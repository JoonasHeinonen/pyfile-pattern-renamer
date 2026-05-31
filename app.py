import os
import re
import unicodedata

directory = "Users\\joona\\Desktop\\development\\koekelberg\\"
file = ""

def main():
    #Main function that calls the directory_file and read_file functions to read a file from a directory.
    directory_file(file, directory)
    read_file()
    rename_file(file)

# Example directory structure to use when opening a file/directory:
# "D:\\myfiles\welcome.txt")
# Actual directory:
# C:\Users\joona\Desktop\development\koekelberg\template.txt
# f = open(directory + "/demofile.txt")
def directory_file(f, d):
    #Opens a file from a directory and reads it.

    #Parameters:
    #    f (str):The name of the file to be opened.
    #    d (str):The directory where the file is located.

    global directory, file
    f = input("Enter the file name: ")

    file = f

def normalize_filename(filename):
    #Normalizes a filename by removing special characters and converting it to lowercase.

    #Parameters:
    #    filename (str): The name of the file to be normalized.

    normalized = unicodedata.normalize('NFKD', filename)
    normalized = normalized.encode('ascii', 'ignore').decode('ascii')
    normalized = normalized.lower()
    normalized = re.sub(r'[\W_]+', '_', normalized)
    return normalized.strip('_')

def rename_file(f):
    #Renames a file in the directory to a normalized version of its name.
    #Parameters:
    #    f (str): The name of the file to be renamed.

    global directory, file
    normalized_name = normalize_filename(f)
    print("Renamed file name from '" + f + "' to '" + normalized_name + "'.")
    f = os.rename("C:\\" + directory + "\\" + file, "C:\\" +  directory + "\\" + normalized_name)
    file = f

def read_file():
    #Reads the file that was opened in the directory_file function.
    f = open("C:\\" + directory + "\\" + file)
    print(f.read())

main()