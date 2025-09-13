import json
import os


def read_transactions(file_path: str) -> list[dict]:
    """
    Считывает список транзакций из JSON-файла.

    Функция проверяет существование файла по указанному пути.
    Если файл не существует, возвращается пустой список.
    Если файл существует, загружает данные и проверяет, что они являются списком.
    В противном случае также возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        if not data or not isinstance(data, list):
            return []
        return data


# def get_transaction_amount(transaction):
#     """
#     Возвращает сумму транзакции в рублях как float.
#     В случае отсутствия или ошибок — 0.
#     """
#     try:
#         amount = transaction.get('amount', 0)
#         currency = transaction.get('currency', 'RUB')
#         return convert_to_rub(amount, currency) or 0.0
#     except Exception:
#         return 0.0
