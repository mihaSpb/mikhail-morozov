# Расчёт среднего балла студента
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Получение среднего балла студента
def get_student_average(student):
    return calculate_average(student["grades"])

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


def main():
    students = [
        {"name": "Daenerys", "grades": [80, 90, 78]},
        {"name": "Tyrion", "grades": [95, 90, 97]},
        {"name": "Joffrey", "grades": [60, 70, 64]},
        {"name": "Arya", "grades": [75, 95, 90]},
        {"name": "Hodor", "grades": [55, 80, 75]}
    ]

    print("Информация по каждому студенту:")
    for student in students:
        student_info(student)

    avgerage_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {avgerage_all:.2f}\n")

    # Добавление нового студента
    new_student = {"name": "Jon", "grades": [70, 80, 75]}
    students.append(new_student)
    print("После добавления нового студента:")
    for student in students:
        student_info(student)
    avgerage_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {avgerage_all:.2f}\n")

    # Удаление студента с самым низким средним баллом
    student_to_remove = min(students, key=get_student_average)
    students.remove(student_to_remove)
    print(f"Удален студент с наименьшим средним баллом: {student_to_remove['name']}\n")

    # Пересчет и вывод общего среднего балла после обновления списка студентов
    print("После удаления студента:")
    for student in students:
        student_info(student)
    avgerage_all = calculate_average_all(students)
    print(f"Общий средний балл по всем студентам: {avgerage_all:.2f}")



main()