directory = ""
file = ""

def main():
    #Main function that calls the directory_file and read_file functions to read a file from a directory.
    directory_file(file, directory)
    read_file()

def directory_file(f, d):
    #Opens a file from a directory and reads it.

    #Parameters:
    #    f (str):The name of the file to be opened.
    #    d (str):The directory where the file is located.

    global directory, file
    d = input("Enter the repository directory: ")
    f = input("Enter the file name: ")

    directory = d
    file = f

def read_file():
    #Reads the file that was opened in the directory_file function.
    f = open("C:\\" + directory + "\\" + file)
    print(f.read())

main()