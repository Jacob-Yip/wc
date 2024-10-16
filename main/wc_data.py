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

    def __str__(self) -> str:
        return f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n{self.__line_count}    {self.__word_count}    {self.__byte_count}    {self.__file_path}"
