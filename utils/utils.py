import os


class Utils:
    def __init__(self) -> None:
        pass

    @classmethod
    def is_file_path_valid(cls, file_path):
        if file_path == "-" or file_path == "":
            return False
        else:
            # Try finding the file based on the file path
            return os.path.isfile(file_path)
