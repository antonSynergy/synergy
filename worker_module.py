import datetime

class WORKER:
    """
    Класс, описывающий работника организации АО 'КИВИ'.
    """
    
    def __init__(self, surname_initials="", position="", salary=0.0, year_hired=2020):
        """
        Конструктор с параметрами (также работает как конструктор по умолчанию,
        если аргументы не переданы).
        """
        self.__surname_initials = surname_initials
        self.__position = position
        self.__salary = salary
        self.__year_hired = year_hired

    # --- Геттеры и Сеттеры (методы изменения и доступа) ---

    @property
    def surname_initials(self):
        return self.__surname_initials

    @surname_initials.setter
    def surname_initials(self, value):
        if isinstance(value, str) and value:
            self.__surname_initials = value
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
            raise ValueError("Зарплата должна быть неотрицательным числом.")

    @property
    def year_hired(self):
        return self.__year_hired

    @year_hired.setter
    def year_hired(self, value):
        current_year = datetime.datetime.now().year
        if isinstance(value, int) and 1950 <= value <= current_year:
            self.__year_hired = value
        else:
            raise ValueError(f"Год поступления должен быть в диапазоне от 1950 до {current_year}.")

    # --- Методы класса ---

    def display(self):
        """
        Метод отображения полей класса.
        """
        print(f"| {self.__surname_initials:<20} | {self.__position:<25} | {self.__salary:>10.2f} руб. | {self.__year_hired} г. |")

    def get_experience(self):
        """
        Возвращает стаж работы в годах.
        """
        current_year = datetime.datetime.now().year
        return current_year - self.__year_hired

    def __del__(self):
        """
        Деструктор (вызывается при удалении объекта сборщиком мусора).
        """
        # В учебных целях просто выводим сообщение
        # print(f"Объект работник {self.__surname_initials} удален из памяти.")
        pass

    def __str__(self):
        return f"{self.__surname_initials} ({self.__position})"
