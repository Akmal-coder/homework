import unittest
from unittest.mock import patch, mock_open
import src.bank_utils


class TestBankUtils(unittest.TestCase):

    def test_process_bank_search_empty(self):
        data = []
        result = src.bank_utils.process_bank_search(data, "test")
        self.assertEqual(result, [])

    def test_process_bank_search_found(self):
        data = [
            {"description": "оплата в магазине", "amount": "100 руб."},
            {"description": "перевод другу", "amount": "200 руб."},
        ]
        res = src.bank_utils.process_bank_search(data, "магазин")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["description"], "оплата в магазине")

    def test_load_json_valid(self):
        # Мок файлового открытия и json.load
        example_json = '[{"key": "value"}]'
        with patch("builtins.open", mock_open(read_data=example_json)):
            data = src.bank_utils.load_json("dummy.json")
            self.assertIsInstance(data, list)
            self.assertEqual(data[0]["key"], "value")

    # Аналогично для load_csv и load_xlsx можно проверить загрузку с моками.


if __name__ == "__main__":
    unittest.main()
