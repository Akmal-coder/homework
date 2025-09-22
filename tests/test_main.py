import unittest
from unittest.mock import patch
from datetime import datetime
import src.main


class TestMainFunctions(unittest.TestCase):

    def test_parse_date_valid(self):
        date = src.main.parse_date("25.12.2023")
        self.assertEqual(date, datetime(2023, 12, 25))

    def test_parse_date_invalid(self):
        date = src.main.parse_date("invalid-date")
        # В нашем коде для ошибки возвращается datetime.min
        self.assertEqual(date, datetime.min)

    def test_clean_record(self):
        rec = {" State ": "executed", "Date ": "01.01.2023 ", "Amount": 100}
        clean = {k.strip().lower(): v for k, v in rec.items()}
        self.assertIn("state", clean)
        self.assertEqual(clean["state"], "executed")

    def test_status_filtering(self):
        data = [
            {"state": "EXECUTED"},
            {"state": "CANCELED"},
            {"state": None},  # Проверка обработки None
            {"state": "executed"},
        ]
        status_input = "EXECUTED"
        filtered = [d for d in data if (d.get("state") or "").upper() == status_input]
        self.assertEqual(len(filtered), 2)

    # Тест выбора файла с моками ввода
    @patch("builtins.input", side_effect=["1"])
    def test_select_file_json(self, mock_input):
        filename, ftype = src.main.select_file()
        self.assertTrue(filename.endswith("operations.json"))
        self.assertEqual(ftype, "json")

    @patch("builtins.input", side_effect=["invalid"])
    def test_select_file_invalid(self, mock_input):
        with self.assertRaises(SystemExit):
            src.main.select_file()


if __name__ == "__main__":
    unittest.main()
