from total_salary_file import total_salary

try:
    total, average = total_salary()
    print(f"загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError as error:
    print(f"Помилка: {error}")
except Exception as error:
    print(f"Помилка: {error}")        