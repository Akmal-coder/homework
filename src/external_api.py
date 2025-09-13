import os
import requests
from typing import Optional
from dotenv import load_dotenv


load_dotenv()


def convert(transaction: dict) -> Optional[float]:
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if currency == "RUB":
        return amount

    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": os.getenv("API_KEY")}
    params = {"from": currency, "to": "RUB", "amount": amount}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result")
    except (requests.RequestException, ValueError) as e:
        print(f"Ошибка при конвертации валюты: {e}")
        return None


if __name__ == "__main__":
    sample_transaction = {
        "date": "2019-08-16T04:23:41.621065",
        "description": "Перевод с карты на счет",
        "from": "MasterCard 8826230888662405",
        "id": 86608620,
        "operationAmount": {"amount": "100.00", "currency": {"code": "USD", "name": "руб."}},
        "state": "EXECUTED",
        "to": "Счет 96119739109420349721",
    }
    print(convert(sample_transaction))
