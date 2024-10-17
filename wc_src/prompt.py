"""
This programme prompts user to provide a file path until he inputs "no"

Command to run the programme
- python -m wc.prompt (-m treats this file as a module from a package so that we can import WC)
"""

from wc_src.main.python.wc import WC

if __name__ == "__main__":
    again = True
    while again:
        try:
            file_path = str(input("Please enter a valid file path: \n"))
            wc = WC(file_path=file_path)
            wc_data = wc.get_wc()
            print(f"{wc_data}\n")

            again_answer = str(
                input("Again? Type \"no\" to terminate programme\n"))
            if again_answer.lower() == "no" or again_answer.lower() == "n":
                again = False
                break
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
            continue

    print(f"Programme terminated gracefully ...")
