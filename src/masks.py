def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX."""
    card_str: str = str(card_number)
    if len(card_str) == 16:
        mask_number = f"{card_str[:4]} {card_str[4:6]} ** **** {card_str[12:]}"
        return mask_number
    return "Некорректный ввод"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX."""
    account_str: str = str(account_number)
    if len(account_str) >= 4:
        mask_account = f"**{account_str[-4:]}"
        return mask_account
    return "Некорректный ввод"


if __name__ == "__main__":
    # Пример вызова функций и вывод результатов
    card_num = 1234567890123456
    account_num = 1234567890123456

    print("Маска номера карты:", get_mask_card_number(card_num))
    print("Маска номера счета:", get_mask_account(account_num))
