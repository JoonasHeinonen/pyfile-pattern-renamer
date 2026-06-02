from importlib.metadata import files
import os
import re
import unicodedata
from gui import GUI

# Set the directory to the folder you want to normalize.
directory = r"C:\Users\joona\Desktop\development\koekelberg\Sprites\badfiles"

def main():
    dir_path = directory
    files = list_directory_files(dir_path)
    if not files:
        return
    rename_files(dir_path, files)
    gui = GUI(files, dir_path)
    gui.run()

def directory_file(f, d):
    #Opens a file from a directory and reads it.

    #Parameters:
    #    f (str):The name of the file to be opened.
    #    d (str):The directory where the file is located.

    global directory, file
    f = input("Enter the file name: ")

    file = f

def list_directory_files(dir_path):
    print("Directory: ", dir_path)

    try:
        dir_list = os.listdir(dir_path)
    except FileNotFoundError:
        print("Directory not found:", dir_path)
        return []

    files = [f for f in dir_list if os.path.isfile(os.path.join(dir_path, f))]
    if not files:
        print("No files found in directory.")
        return []

    print("Files in directory:")
    print(*files, sep="\n")

    print("Normalized file names:")
    print(*[normalize_filename(f) for f in files], sep="\n")

    return files

def normalize_filename(filename):
    base, ext = os.path.splitext(filename)
    normalized = unicodedata.normalize("NFKD", base)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower()
    normalized = re.sub(r"[\W_]+", "_", normalized)
    normalized = normalized.strip("_")
    return normalized + ext.lower()

def rename_file(dir_path, filename):
    normalized_name = normalize_filename(filename)
    old_path = os.path.join(dir_path, filename)
    new_path = os.path.join(dir_path, normalized_name)

    if old_path == new_path:
        print("Skipping already normalized file:", filename)
        return

    if os.path.normcase(old_path) == os.path.normcase(new_path):
        # Case-only rename on Windows requires an intermediate path.
        temp_path = os.path.join(dir_path, f".{filename}.rename.tmp")
        try:
            os.rename(old_path, temp_path)
            os.rename(temp_path, new_path)
            print("Renamed '{}' -> '{}'".format(filename, normalized_name))
        except OSError as exc:
            print("Failed to rename {}: {}".format(filename, exc))
        return

    if os.path.exists(new_path):
        print("Skipping rename because target already exists:", new_path)
        return

    try:
        os.rename(old_path, new_path)
        print("Renamed '{}' -> '{}'".format(filename, normalized_name))
    except OSError as exc:
        print("Failed to rename {}: {}".format(filename, exc))

def read_file():
    #Reads the file that was opened in the directory_file function.
    f = open(directory + "\\" + file)
    print(f.read())

def rename_files(dir_path, files):
    for f in files:
        rename_file(dir_path, f)

main()