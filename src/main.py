import sys
from datetime import datetime
from src.bank_utils import load_json, load_csv, load_xlsx, process_bank_search


def select_file() -> (str, str):
    """
    Выбирает файл для загрузки, исходя из пользовательского выбора.

    """
    print("Выберите файл для загрузки:")
    print("1. JSON (operations.json)")
    print("2. CSV (transactions.csv)")
    print("3. XLSX (transactions_excel.xlsx)")
    choice = input().strip()
    if choice == "1":
        return "../data/operations.json", "json"
    elif choice == "2":
        return "../data/transactions.csv", "csv"
    elif choice == "3":
        return "../data/transactions_excel.xlsx", "xlsx"
    else:
        print("Некорректный выбор")
        sys.exit(1)


def parse_date(date_str):
    """
    Преобразует строку даты в объект datetime.
    В случае ошибки возвращает минимальную дату.

    """
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except Exception:
        return datetime.min


def main():
    """
    Основная функция программы.
    Выполняет последовательность загрузки данных, их очистки,
    фильтрации и вывода итогового списка транзакций.
    """
    print("Программа: Добро пожаловать!")

    filename, ftype = select_file()

    if ftype == "json":
        data = load_json(filename)
    elif ftype == "csv":
        data = load_csv(filename)
    elif ftype == "xlsx":
        data = load_xlsx(filename)
    else:
        print("Неподдерживаемый формат файла.")
        sys.exit(1)

    def clean_record(rec):
        """
        Очищает запись: убирает лишние пробелы, делает ключи строчными.

        """
        return {k.strip().lower(): v for k, v in rec.items()}

    data = [clean_record(rec) for rec in data]

    print(f"Всего записей: {len(data)}.")

    # Фильтрация по статусу операции
    statuses = {"EXECUTED", "CANCELED", "PENDING"}
    status_input = input("Введите статус операции для фильтрации (EXECUTED, CANCELED, PENDING):\n").strip().upper()
    if status_input not in statuses:
        print("Некорректный статус. Выход.")
        sys.exit(1)
    data = [d for d in data if (d.get("state") or "").upper() == status_input]
    print(f"Операций после фильтрации по статусу: {len(data)}")

    # Сортировка по дате
    sort_resp = input("Отсортировать по дате? (да/нет):\n").strip().lower()
    if sort_resp == "да":
        order = input("По возрастанию или по убыванию? (введите 'в' или 'у'): ").strip().lower()
        reverse_order = order == "у"
        data.sort(key=lambda d: parse_date(d.get("date", "")), reverse=reverse_order)

    # Фильтрация только рублёвых операций
    rubles_only = input("Выводить только рублевые операции? (да/нет):\n").strip().lower()
    if rubles_only == "да":
        data = [d for d in data if "руб." in str(d.get("amount", "")).lower()]

    # Фильтр по слову в описании
    search_word_choice = input("Фильтр по слову в описании? (да/нет):\n").strip().lower()
    if search_word_choice == "да":
        word = input("Введите слово для поиска:\n").strip()
        data = process_bank_search(data, word)

    print(f"\nИТОГОВЫЙ список ({len(data)} транзакций):\n")
    if len(data) == 0:
        print("Нет транзакций по заданным фильтрам.")
    else:
        for d in data:
            date = d.get("date", "")
            description = d.get("description", "")
            amount = d.get("amount", "")
            print(f"{date} {description}\nСумма: {amount}\n")


if __name__ == "__main__":
    main()

#
#
#
#
#
#
# from transaction_loaders import read_transactions_csv, read_transactions_excel
#
#
# def main():
#     # Пример пути к CSV файлу
#     csv_path = "../data/transactions.csv"
#     transactions_from_csv = read_transactions_csv(csv_path)
#     print("Транзакции из CSV:")
#     for t in transactions_from_csv:
#         print(t)
#
#     # Пример пути к Excel файлу
#     excel_path = "data/transactions.xlsx"
#     transactions_from_excel = read_transactions_excel(excel_path)
#     print("\nТранзакции из Excel:")
#     for t in transactions_from_excel:
#         print(t)
#
#
# if __name__ == "__main__":
#     main()


# from utils import read_transactions
#
#
# if __name__ == "__main__":
#     print(read_transactions("../data/operations.json"))
