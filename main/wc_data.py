"""
The class representing the result of the wc programme
"""
from utils.utils import Utils


class WCData:
    def __init__(self, line_count: int, word_count: int, byte_count: int, file_path: str) -> None:
        if line_count < 0:
            raise Exception(f"Invalid line count: {line_count}")
        else:
            self.__line_count = line_count

        if word_count < 0:
            raise Exception(f"Invalid word_count: {word_count}")
        else:
            self.__word_count = word_count

        if byte_count < 0:
            raise Exception(f"Invalid byte count: {byte_count}")
        else:
            self.__byte_count = byte_count

        if not Utils.is_file_path_valid(file_path=file_path):
            raise Exception(f"Invalid file: {file_path}")
        else:
            self.__file_path = file_path

    @property
    def line_count(self):
        return self.__line_count

    @property
    def word_count(self):
        return self.__word_count

    @property
    def byte_count(self):
        return self.__byte_count

    @property
    def file_path(self):
        return self.__file_path

    def __str__(self) -> str:
        return f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n{self.__line_count}    {self.__word_count}    {self.__byte_count}    {self.__file_path}"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, WCData):
            return False
        else:
            if not __value.line_count == self.__line_count:
                return False

            if not __value.word_count == self.__word_count:
                return False

            if not __value.byte_count == self.__byte_count:
                return False

            # We do not care about file_path here

            return True
