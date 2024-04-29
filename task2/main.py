from get_cats_info import get_cats_info
import json

def main():
    try:
       cats_info = get_cats_info("task2/cats_file.txt")
       json_string = json.dumps(cats_info, indent=4)
       print(json_string)
    except FileNotFoundError as error:
       print(f"Помилка: {error}")
    except Exception as error:
       print(f"Помилка: {error}")  

if __name__ == "__main__":
   main()          