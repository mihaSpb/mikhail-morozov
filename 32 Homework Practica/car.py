import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    @classmethod
    def from_vin(cls, vin):
        """
        Простой пример "декодирования" VIN-кода. В реальном мире процесс гораздо сложнее.
        Здесь для простоты используем фиктивные данные.
        """
        # Например, можно использовать определённые части VIN для определения характеристик.
        # Для примера просто возвращаем заготовленные данные:
        make = "Toyota"
        model = "Camry"
        year = 2018
        return cls(make, model, year)

    @staticmethod
    def is_valid_year(year):
        """
        Проверяет, что год выпуска находится в допустимом диапазоне: от 1886 до текущего года.
        """
        current_year = datetime.datetime.now().year
        return 1886 <= year <= current_year
