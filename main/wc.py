"""
The programme that counts the word count of the text in a file
Input format: python ./driver.py <filename>
Output format:linecount    wordcount    bytecount   filepath
"""
import os
from main.wc_data import WCData
from utils.utils import Utils


class WC:
    def __init__(self, file_path: str) -> None:
        if not Utils.is_file_path_valid(file_path=file_path):
            raise Exception(f"Invalid file: {file_path}")

        self.__file_path = file_path

        try:
            self.__file = open(self.__file_path, "rt")

            print(f"========== TEST ================")
            print(
                f"\nFile exist? = {Utils.is_file_path_valid(file_path=file_path)}")
            f = open("resource/test/test_valid_file_path.txt", "rt")
            f.seek(0)
            lines = f.readlines()
            f.close()
            print(f"FFFFFFF.lines = {lines}\n")
            print(f"==========================")

            self.__file.seek(0)  # Just in case
            self.__lines = self.__file.readlines()
            print(f"lines = {self.__lines}; file_path = {self.__file_path}")
        except Exception as e:
            raise Exception(f"Error in reading {self.__file_path}: {e}")
        finally:
            self.__file.close()

        self.__wc_data = None

    def get_wc(self) -> WCData:
        try:
            self.__wc_data = WCData(
                line_count=self.get_line_count(),
                word_count=self.get_word_count(),
                byte_count=self.get_byte_count(),
                file_path=self.__file_path
            )

            return self.__wc_data
        except Exception as e:
            raise Exception(f"Error in get_wc(): {e}")

    def get_line_count(self) -> int:
        return len(self.__lines)

    def get_word_count(self) -> int:
        word_count = 0

        for line in self.__lines:
            words = line.split()
            word_count += len(words)

        return word_count

    def get_byte_count(self) -> int:
        file_stats = os.stat(self.__file_path)
        # print(f"flie_stats = {file_stats}")
        return file_stats.st_size
