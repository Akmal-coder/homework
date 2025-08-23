import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def mask_sample():
    return "7000 79** **** 6361"


@pytest.fixture
def account_mask_sample():
    return "**4305"


@pytest.mark.parametrize(
    "input_str, substrings",
    [
        ("Visa Platinum 7000792289606361", ["Visa Platinum", "7000", "**", "6361"]),
        ("Maestro 1596837868705199", ["Maestro", "1596"]),
        ("Счет 73654108430135874305", ["Счет", "**4305"]),
        ("Некорректный формат", ["Некорректный формат"]),
        ("", [""]),
    ],
)
def test_mask_account_card(input_str, substrings):
    result = mask_account_card(input_str)
    for s in substrings:
        assert s in result


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("невалидная дата", ""),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
