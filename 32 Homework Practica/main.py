from car import Car

def main():
    # Создаем объект автомобиля с использованием конструктора __init__
    car1 = Car("Ford", "Mustang", 2022)
    print("Информация об автомобиле (конструктор):")
    print(car1.get_info())

    # Создаем объект автомобиля с использованием классового метода from_vin
    vin_code = "1HGCM82633A004352"  # Пример VIN-кода
    car2 = Car.from_vin(vin_code)
    print("\nИнформация об автомобиле (по VIN):")
    print(car2.get_info())

    # Проверяем корректность года выпуска с помощью статического метода is_valid_year
    year_to_check = 2025
    if Car.is_valid_year(year_to_check):
        print(f"\nГод {year_to_check} корректен для выпуска автомобиля.")
    else:
        print(f"\nГод {year_to_check} некорректен для выпуска автомобиля.")

if __name__ == "__main__":
    main()
