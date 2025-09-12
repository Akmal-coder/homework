import os

import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv()


def convert(currency: str, amount) -> Any:
    """
    Конвертирует сумму из валюты транзакции в российские рубли (RUB).

    Если валюта транзакции уже в RUB, возвращается исходная сумма без конвертации.
    Иначе выполняется запрос к API exchangerates_data для получения конвертированной суммы.
    """

    # currency = transaction["operationAmount"]["currency"]["code"]
    # amount = ["operationAmount"]["amount"]
    # if currency == "RUB":
    #     return amount
    to_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={currency}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}
    # print(headers)
    # params = {"from": to_currency, "to": "RUB", "amount": amount}

    response = requests.get(url, headers=headers, data={})
    return response.json().get("result")


if __name__ == "__main__":
    print(convert("USD", "125"))
