from worker import WORKER
import sys

def input_worker_data():
    """
    Функция для ввода данных о работнике с клавиатуры.
    """
    print("\n--- Ввод данных нового сотрудника ---")
    try:
        surname = input("Введите Фамилию и Инициалы (например, Иванов И.И.): ")
        position = input("Введите должность: ")
        salary = float(input("Введите зарплату: "))
        year_hired = int(input("Введите год поступления на работу: "))
        
        # Создаем объект класса WORKER
        new_worker = WORKER(surname, position, salary, year_hired)
        return new_worker
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
        return None

def main():
    # Используем стандартный список List для хранения объектов
    workers_list = []
    
    # Добавим несколько тестовых данных для примера (чтобы не вводить все вручную)
    # Данные адаптированы под АО КИВИ
    test_workers = [
        WORKER("Петров А.С.", "Разработчик Python", 180000, 2018),
        WORKER("Сидорова Е.В.", "Специалист комплаенс", 150000, 2020),
        WORKER("Иванов Д.М.", "Junior Analyst", 90000, 2023),
        WORKER("Кузнецова О.Н.", "HR-менеджер", 120000, 2015),
        WORKER("Смирнов К.Л.", "DevOps Engineer", 210000, 2019)
    ]
    
    workers_list.extend(test_workers)

    print("="*75)
    print(f"{'Список сотрудников АО \"КИВИ\"':^75}")
    print("="*75)
    print(f"| {'ФИО':<20} | {'Должность':<25} | {'Зарплата':>10} | {'Год приема':<8} |")
    print("-"*75)
    
    for worker in workers_list:
        worker.display()
    
    print("="*75)

    # Меню выбора действия
    while True:
        print("\nВыберите действие:")
        print("1. Добавить нового сотрудника")
        print("2. Найти сотрудников со стажем больше указанного")
        print("3. Выход")
        
        choice = input("Ваш выбор (1-3): ")
        
        if choice == '1':
            new_w = input_worker_data()
            if new_w:
                workers_list.append(new_w)
                print("Сотрудник успешно добавлен.")
                
        elif choice == '2':
            try:
                min_experience = int(input("Введите минимальный стаж работы (в годах): "))
                found_workers = []
                
                print(f"\n--- Сотрудники со стажем более {min_experience} лет ---")
                print(f"| {'ФИО':<20} | {'Должность':<25} | {'Стаж (лет)':<10} |")
                print("-"*60)
                
                for worker in workers_list:
                    experience = worker.get_experience()
                    if experience > min_experience:
                        worker.display_short() if hasattr(worker, 'display_short') else print(f"| {worker.surname_initials:<20} | {worker.position:<25} | {experience:<10} |")
                        found_workers.append(worker)
                
                print("-"*60)
                
                if not found_workers:
                    print("Сообщение: Сотрудников с таким стажем не найдено.")
                    
            except ValueError:
                print("Ошибка: Пожалуйста, введите целое число для стажа.")
                
        elif choice == '3':
            print("Завершение программы...")
            # Принудительное очищение списка (вызов деструкторов)
            workers_list.clear()
            sys.exit(0)
            
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
