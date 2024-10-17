"""
This programme prompts user to provide a file path until he inputs "no"

Command to run the programme
- python -m wc_src.prompt (-m treats this file as a module from a package so that we can import WC)
"""
from main.python.wc import WC

FILE_PATH = "./main/resource/text.txt"

if __name__ == "__main__":
    try:
        wc = WC(file_path=FILE_PATH)
        wc_data = wc.get_wc()
        print(f"{wc_data}\n")
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

    print(f"Programme terminated gracefully ...")
