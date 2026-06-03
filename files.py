import os
import re
import unicodedata

class Files:

    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files = []
    
    def convert_files(self, mode):
        files = self.list_directory_files(self.dir_path)
        if not files:
            return
        self.rename_files(self.dir_path, files, mode)

    def list_directory_files(self, dir_path):
        try:
            dir_list = os.listdir(dir_path)
        except FileNotFoundError:
            return []

        files = [f for f in dir_list if os.path.isfile(os.path.join(dir_path, f))]
        if not files:
            return []

        return files
    
    # Define a function to convert a string to camel case
    def camel_case(self, s):
        # Use regular expression substitution to replace underscores and hyphens with spaces,
        # then title case the string (capitalize the first letter of each word), and remove spaces
        s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
        
        # Join the string, ensuring the first letter is lowercase
        return ''.join([s[0].lower(), s[1:]])

    def normalize_filename(self, filename, mode):
        match mode:
            case 'camel_case':
                base, ext = os.path.splitext(filename)
                normalized = self.camel_case(base)
                return normalized + ext.lower()
            case 'snake_case':
                base, ext = os.path.splitext(filename)
                normalized = unicodedata.normalize("NFKD", base)
                normalized = normalized.encode("ascii", "ignore").decode("ascii")
                normalized = normalized.lower()
                normalized = re.sub(r"[\W_]+", "_", normalized)
                normalized = normalized.strip("_")
                return normalized + ext.lower()
            case _:
                return filename

    def rename_file(self, dir_path, mode, filename):
        print("Renaming file: ", mode)
        normalized_name = self.normalize_filename(filename, mode)
        old_path = os.path.join(dir_path, filename)
        new_path = os.path.join(dir_path, normalized_name)

        if old_path == new_path:
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

    def rename_files(self, dir_path, files, mode):
        print("JavaScript in camelCase: ", self.camel_case('Java_Script'))
        for f in files:
            self.rename_file(dir_path, mode, f)