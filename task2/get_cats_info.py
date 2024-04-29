def get_cats_info(path):
    cats_info = []

    try:
        with open("task2\\cats_info.txt", 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cats_info.append({
                            "id": cat_id,
                            "name": name,
                            "age": age
                        })
                    else: 
                        print(f"Помилка: Некоректний формат рядку: {line}")
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
    except Exception as error:
        print(f"Помилка: {error}")

    return cats_info                                
                    