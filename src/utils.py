import json
import os
import logging


LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(f"../logs/utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


def read_transactions(file_path: str) -> list[dict]:
    """
    Считывает список транзакций из JSON-файла.
    При ошибках или отсутствии файла возвращает пустой список.
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}. Возвращен пустой список.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data or not isinstance(data, list):
            logger.error(f"Данные из файла {file_path} не являются списком или пусты.")
            return []

        logger.debug(f"Транзакции успешно загружены из файла {file_path}. Количество записей: {len(data)}")
        return data

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON из файла {file_path}: {e}")
        return []

    except Exception as e:
        logger.error(f"Неизвестная ошибка при чтении файла {file_path}: {e}")
        return []


# import json
# import os
#
#
# def read_transactions(file_path: str) -> list[dict]:
#     """
#     Считывает список транзакций из JSON-файла.
#
#     Функция проверяет существование файла по указанному пути.
#     Если файл не существует, возвращается пустой список.
#     Если файл существует, загружает данные и проверяет, что они являются списком.
#     В противном случае также возвращает пустой список.
#     """
#     if not os.path.exists(file_path):
#         return []
#
#     with open(file_path, "r", encoding="utf-8") as file:
#         data = json.load(file)
#         if not data or not isinstance(data, list):
#             return []
#         return data


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
