import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фикстура с примером транзакций
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Transaction in USD",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 2,
            "description": "Transaction in EUR",
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "EUR", "code": "EUR"}
            }
        },
        {
            "id": 3,
            "description": "Another USD transaction",
            "operationAmount": {
                "amount": "150",
                "currency": {"name": "USD", "code": "USD"}
            }
        }
    ]

# Параметризация для теста фильтрации по валюте
@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("RUB", [])
])
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [tx["id"] for tx in result]
    assert result_ids == expected_ids

# Тест для функции описаний транзакций
def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Transaction in USD",
        "Transaction in EUR",
        "Another USD transaction"
    ]
    assert descriptions == expected_descriptions

# Параметризация для генератора номеров карт
@pytest.mark.parametrize("start, stop, expected_numbers", [
    (
        1,
        3,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    ),
    (
        2,
        3,
        [
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    )
])
def test_card_number_generator(start, stop, expected_numbers):
    gen = card_number_generator(start, stop)
    generated_numbers = list(gen)
    assert generated_numbers == expected_numbers

# Тест для проверки формата номера карты
def test_card_number_format():
    gen = card_number_generator(1, 3)
    card_number = next(gen)
    # Проверка, что номер состоит из 4 групп по 4 цифры
    parts = card_number.split()
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()