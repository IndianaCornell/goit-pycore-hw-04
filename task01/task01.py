# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
 
import re

def total_salary(path):
    try:
     with open(path, encoding="utf-8") as f: 
          users_list = [el.strip() for el in f.readlines()]
          users_count = len(users_list)
          salary_sum = 0

          if users_count: 
               for user in users_list:
                    pattern = r"[\D]"
                    salary = re.sub(pattern, "", user)
                    salary_sum += int(salary)

               average_salary = int(salary_sum/users_count)
               print(f"Загальна сума заробітної плати: {salary_sum}, Середня заробітна плата: {average_salary}")
          else:
               print("Ваш текстовий файл порожній.")
    except FileNotFoundError: 
        print("Файл не знайдено.")        

total_salary("task01/salary_file.txt")
