import logging
import os



# Настройка папки и логгера
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(f"../logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Избегаем дублирования, если модуль импортируется несколько раз
if not logger.hasHandlers():
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты в формате XXXX XX** **** XXXX
    """
    try:
        card_number_str = str(card_number)
        if len(card_number_str) != 16:
            raise ValueError("Неверная длина номера")

        card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
        card_mask = " ".join(card_mask[i: i + 4] for i in range(0, len(card_mask), 4))

        logger.debug(f"Маска номера карты сформирована успешно: {card_mask}")
        return card_mask

    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера аккаунта в формате **XXXX
    """
    try:
        account_number_str = str(account_number)

        if len(account_number_str) != 20:
            raise ValueError("Неверная длина номера")

        mask_account = "**" + account_number_str[-4:]
        logger.debug(f"Маска номера аккаунта сформирована успешно: {mask_account}")
        return mask_account

    except Exception as e:
        logger.error(f"Ошибка при маскировании номера аккаунта: {e}")
        raise






























# def get_mask_card_number(card_number: int) -> str:
#     """
#     Возвращает маску номера карты в формате XXXX XX** **** XXXX
#     """
#     card_number_str = str(card_number)
#     if len(card_number_str) != 16:
#         raise ValueError("Неверная длина номера")
#
#     card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
#     card_mask = " ".join(card_mask[i : i + 4] for i in range(0, len(card_mask), 4))
#     return card_mask
#
#
# def get_mask_account(account_number: int) -> str:
#     """
#     Возвращает маску номера аккаунта в формате **XXXX
#     """
#     account_number_str = str(account_number)
#
#     if len(account_number_str) != 20:
#         raise ValueError("Неверная длина номера")
#
#     mask_account = "**" + account_number_str[-4:]
#     return mask_account
