import sys
from main.wc import WC

FILE_PATH = "resource/text.txt"  # Default file path

if __name__ == "__main__":
    # Main programme
    arguments = sys.argv

    assert (len(arguments) == 1 or len(arguments) ==
            2), f"Invalid command format: python driver.py <file_path> or python ./driver.py expected"

    # Create an instance of WC
    if len(arguments) == 2:
        FILE_PATH = arguments[1]

    wc = WC(file_path=FILE_PATH)
    wc_data = wc.get_wc()

    # Print result
    print(wc_data)
