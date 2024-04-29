import os
from colorama import Fore, Style

def display_directory_structure(directory_path):
    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(Fore.BLUE + entry.name + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + entry.name + Style.RESET_ALL)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except NotADirectoryError:
        print(f"Error: '{directory_path}' is not a directory.")