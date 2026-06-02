from importlib.metadata import files
import os
import re
import unicodedata

class Files:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files = []

    def list_directory_files(self, dir_path):
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
        print(*[self.normalize_filename(f) for f in files], sep="\n")

        return files

    def normalize_filename(self,filename):
        base, ext = os.path.splitext(filename)
        normalized = unicodedata.normalize("NFKD", base)
        normalized = normalized.encode("ascii", "ignore").decode("ascii")
        normalized = normalized.lower()
        normalized = re.sub(r"[\W_]+", "_", normalized)
        normalized = normalized.strip("_")
        return normalized + ext.lower()

    def rename_file(self, dir_path, filename):
        normalized_name = self.normalize_filename(filename)
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

    def rename_files(self, dir_path, files):
        for f in files:
            self.rename_file(dir_path, f)