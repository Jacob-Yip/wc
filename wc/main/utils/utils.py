import os


class Utils:
    def __init__(self) -> None:
        pass

    @classmethod
    def is_file_path_valid(cls, file_path: str):
        # Only accept txt files so far
        if file_path == "-" or file_path == "" or not file_path[-4:] == ".txt":
            return False
        else:
            # Try finding the file based on the file path
            return os.path.isfile(file_path)
