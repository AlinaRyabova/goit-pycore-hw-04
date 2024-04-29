import sys
from directory_structure import display_directory_structure

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py /path/to/directory")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()