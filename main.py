from worker_module import WORKER

def input_worker_data():
    """Функция для ввода данных о работнике с клавиатуры."""
    print("\n--- Ввод данных нового сотрудника ---")
    try:
        fio = input("Введите Фамилию и Инициалы (например, Петров П.П.): ")
        position = input("Введите должность: ")
        salary = float(input("Введите зарплату: "))
        year_start = int(input("Введите год поступления на работу: "))
        
        # Создаем объект класса WORKER
        worker = WORKER(fio, position, salary, year_start)
        return worker
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
        return None

def main():
    # Список для хранения объектов (динамический массив)
    workers_list = []
    
    print("=== Система учета сотрудников Университета 'Синергия' ===")
    
    # 1. Ввод данных (цикл прерывается, если пользователь введет 'stop' в поле ФИО)
    while True:
        worker = input_worker_data()
        if worker:
            workers_list.append(worker)
        
        cont = input("Добавить еще сотрудника? (да/нет): ").lower()
        if cont != 'да':
            break

    # Вывод всех добавленных сотрудников (для наглядности)
    print("\n=== Список всех введенных сотрудников ===")
    if not workers_list:
        print("Список пуст.")
    else:
        for w in workers_list:
            w.display()

    # 2. Поиск сотрудников со стажем больше введенного значения
    try:
        min_experience = int(input("\nВведите минимальный стаж (лет) для поиска: "))
    except ValueError:
        print("Некорректный ввод числа лет.")
        return

    print(f"\n=== Сотрудники со стажем более {min_experience} лет ===")
    found = False
    
    for worker in workers_list:
        experience = worker.get_experience()
        if experience > min_experience:
            worker.display()
            found = True
            
    if not found:
        print("Сотрудников с указанным стажем не найдено.")


if __name__ == "__main__":
    main()
