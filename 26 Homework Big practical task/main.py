# Расчёт среднего балла студента
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Расчёт среднего балла всех студентов
def calculate_average_all(students):
    total_sum = 0
    total_count = 0
    for student in students:
        total_sum += sum(student["grades"])
        total_count += len(student["grades"])
    return total_sum / total_count if total_count != 0 else 0

# Информация о студенте
def student_info(student):
    average = calculate_average(student["grades"])
    status = "Успешен" if average >= 75 else "Отстающий"
    print(f"Студент: {student['name']}")
    print(f"Средний балл: {average:.2f}")
    print(f"Статус: {status}\n")

# Вывод на экран информации о студентах
def print_all_students(students):
    for student in students:
        student_info(student)

# Добавление нового студента
def add_student(students, new_student):
    students.append(new_student)

# Вывод обновленной информацию о студентах
def print_updated_students_info(students):
    print("После добавления нового студента:")
    print_all_students(students)
    average_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {average_all:.2f}\n")

# Удаление студента
def remove_student_with_lowest_average(students):
    student_to_remove = min(students, key=lambda s: calculate_average(s["grades"]))
    students.remove(student_to_remove)
    return student_to_remove


def main():
    students = [
        {"name": "Daenerys", "grades": [80, 90, 78]},
        {"name": "Tyrion", "grades": [95, 90, 97]},
        {"name": "Joffrey", "grades": [60, 70, 64]},
        {"name": "Arya", "grades": [75, 95, 90]},
        {"name": "Hodor", "grades": [55, 80, 75]}
    ]

    print("Информация по каждому студенту:")
    print_all_students(students)

    avgerage_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {avgerage_all:.2f}\n")

    # Добавление нового студента
    new_student = {"name": "Jon", "grades": [70, 80, 75]}
    add_student(students, new_student)
    print_updated_students_info(students)

    # Удаление студента с самым низким средним баллом
    removed_student = remove_student_with_lowest_average(students)
    print(f"Удален студент с наименьшим средним баллом: {removed_student['name']}\n")

    # Пересчет и вывод общего среднего балла после обновления списка студентов
    print("После удаления студента:")
    print_all_students(students)
    average_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {average_all:.2f}")


main()