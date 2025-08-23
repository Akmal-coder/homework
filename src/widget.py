from datetime import datetime
from typing import Optional
#
from src import masks


def mask_account_card(info: str) -> str:
    """
    Обрабатывает строку с информацией о карте или счете и возвращает маскированную версию.

    Аргументы:
        info (str): строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Возвращает:
        str: маскированная строка по типу карты или счета.
    """
    parts = info.strip().split()

    # Проверка, что строка не пустая и разбита на части
    if not parts:
        return ""

    # Обработка случаев с картой (например, "Visa Platinum ..." или "MasterCard ...")
    if parts[0] in ["Visa", "Maestro", "Visa Classic", "Visa Gold", "Visa Platinum"]:
        # Предполагается, что номер карты — последний элемент строки
        card_type = parts[0]
        # Номер карты — последний элемент строки
        card_number = parts[-1]
        masked_number = masks.get_mask_card_number(card_number)
        return f"{info[:info.rfind(card_number)]}{masked_number}"

    # Обработка случаев со счетом ("Счет ...")
    elif parts[0] == "Счет":
        account_number = parts[-1]
        masked_account = masks.get_mask_account(account_number)
        return f"Счет {masked_account}"

    else:
        # Если формат не распознан, возвращаем исходную строку или сообщение об ошибке
        return info


def get_date(date_str: str) -> str:
    """
    Преобразуем строку с датой из формата ISO 8601 в формат DD.MM.YYYY.

    Аргументы:
        date_str (str): строка вида "2024-03-11T02:26:18.671407"

    Возвращает:
        str: дата в формате "11.03.2024"
    """
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return ""  # Или можно вернуть сообщение об ошибке


if __name__ == "__main__":
    # Примеры для mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

    print(mask_account_card("Maestro 1596837868705199"))  # Maestro 1596837868705199 (маска по маскам)

    # Примеры для get_date
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
