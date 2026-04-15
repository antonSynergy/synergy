import datetime

class WORKER:
    """
    Класс, описывающий работника организации.
    """
  
    def __init__(self, fio="", position="", salary=0.0, year_start=2020):
        """
        Конструктор с параметрами (также работает как конструктор по умолчанию,
        если аргументы не переданы).
        """
        self.__fio = fio                   # Фамилия и инициалы
        self.__position = position         # Должность
        self.__salary = salary             # Зарплата
        self.__year_start = year_start     # Год поступления

    # --- Геттеры и Сеттеры (методы изменения и доступа) ---

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        if isinstance(value, str) and value:
            self.__fio = value
        else:
            raise ValueError("ФИО должно быть непустой строкой.")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, str) and value:
            self.__position = value
        else:
            raise ValueError("Должность должна быть непустой строкой.")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__salary = value
        else:
            raise ValueError("Зарплата должна быть положительным числом.")

    @property
    def year_start(self):
        return self.__year_start

    @year_start.setter
    def year_start(self, value):
        current_year = datetime.datetime.now().year
        if isinstance(value, int) and 1950 <= value <= current_year:
            self.__year_start = value
        else:
            raise ValueError(f"Год поступления должен быть в диапазоне от 1950 до {current_year}.")

    # --- Метод отображения полей ---
    def display(self):
        """Вывод информации о работнике на экран."""
        print(f"Сотрудник: {self.__fio}")
        print(f"Должность: {self.__position}")
        print(f"Зарплата: {self.__salary} руб.")
        print(f"Год поступления: {self.__year_start}")
        print("-" * 30)

    # --- Метод расчета стажа ---
    def get_experience(self):
        """Возвращает стаж работы в годах."""
        current_year = datetime.datetime.now().year
        return current_year - self.__year_start

    # --- Деструктор (в Python это __del__) ---
    def __del__(self):
        """
        Деструктор. Вызывается сборщиком мусора при удалении объекта.
        В учебных целях выводим сообщение.
        """
        print(f"[Деструктор] Объект работника {self.__fio} удален из памяти.")


# Тестовый блок (не обязателен, но полезен для проверки модуля)
if __name__ == "__main__":
    w = WORKER("Иванов И.И.", "Преподаватель", 80000, 2018)
    w.display()
