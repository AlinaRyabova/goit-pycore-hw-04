def total_salary():
    total_salary = 0
    developer_count = 0

    try:
        # Відкриваємо файл 'salary_file.txt' для читання'
        with open("task1\\salary_file.txt", 'r', encoding='utf-8') as file:
            # Читаємо файл по рядках
            for line in file:
                # Видаляємо зайві пробіли з початку і кінця рядка
                line = line.strip()  
                if line:
                    # Розділяємо рядок по комі
                    parts = line.split(',')  
                    # Перевіряємо, чи отримано дві частини (прізвище і зарплата)
                    if len(parts) == 2:  
                        try:
                            # Конвертуємо зарплату в ціле число
                            salary = int(parts[1])  
                            # Додаємо зарплату до загальної суми
                            total_salary += salary  
                            # Збільшуємо лічильник розробників
                            developer_count += 1  
                        except ValueError:
                            # Якщо зарплата не є цілим числом, піднімаємо виняток з повідомленням про помилку
                            raise ValueError(f"Некоректне значення заробітної плати у рядку: {line}")
                    else:
                        # Якщо рядок не містить дві частини (прізвище і зарплата), піднімаємо виняток
                        raise ValueError(f"Некоректний формат рядку: {line}")
        
        # Обчислюємо середню заробітну плату
        if developer_count > 0:
            average_salary = total_salary / developer_count
        else:
            average_salary = 0

        # Повертаємо загальну суму заробітної плати і середню заробітну плату у вигляді кортежу
        return total_salary, average_salary

    except FileNotFoundError:
        # Обробляємо виняток, якщо файл 'salary_file.txt' не знайдено
        raise FileNotFoundError("Файл 'salary_file.txt' не знайдено")
    except Exception as error:
        # Обробляємо будь-який інший виняток та піднімаємо власний виняток з повідомленням про помилку
        raise RuntimeError(f"Помилка: {error}")