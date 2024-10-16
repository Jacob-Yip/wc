import sys
from main.wc import WC

FILE_PATH = "resource/text.txt"  # Default file path

if __name__ == "__main__":
    # Main programme
    arguments = sys.argv

    assert (len(arguments) == 1 or len(arguments) ==
            2), f"Invalid command format: python driver.py <file_path> or python ./driver.py"

    # Create an instance of WC
    if len(arguments) == 2:
        FILE_PATH = arguments[1]

    wc = WC(file_path=FILE_PATH)
    wc_data = wc.get_wc()

    # Print result
    print(wc_data)


# if __name__ == "__main__":
#     arguments = sys.argv
#     assert len(
#         arguments) == 2, f"Invalid argument. Expect python3 wc.py <filename>"

#     file_path = arguments[1]

#     wc = WC()

#     if not wc.is_file_path_valid(file_path=file_path):
#         raise Exception(f"File not found: {file_path}")

#     file = open(file_path, "rt")
#     lines = file.readlines()

#     line_count = get_line_count(lines=lines)
#     word_count = get_word_count(lines=lines)
#     byte_count = get_byte_count(file_path=file_path)

#     print(f"{line_count}    {word_count}    {byte_count}    {file_path}")
