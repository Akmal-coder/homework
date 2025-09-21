import unittest
from unittest.mock import patch, mock_open
import json
from src.utils import read_transactions


class TestReadTransactions(unittest.TestCase):
    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_success(self, mock_file_open, mock_os_exists):
        file_path = "../data/operations.json"
        expected_data = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ]
        # Настраиваем поведение заглушек
        mock_os_exists.return_value = True  # Файл существует
        mock_file_open.return_value.read.return_value = json.dumps(expected_data)  # Содержимое файла

        # Вызываем тестируемую функцию
        result = read_transactions(file_path)

        # Проверяем результат
        self.assertEqual(result, expected_data)

        # Проверяем, что os.path.exists был вызван с правильным путем
        mock_os_exists.assert_called_once_with(file_path)

        # Проверяем, что open был вызван с правильными аргументами
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

        # Проверяем, что read был вызван
        mock_file_open.return_value.read.assert_called_once()

    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_empty_json_list(self, mock_file_open, mock_os_exists):
        """
        Тестируем чтение файла, который содержит пустой JSON-список.
        """
        file_path = "../data/operations.json"
        empty_list_data = []

        mock_os_exists.return_value = True
        mock_file_open.return_value.read.return_value = json.dumps(empty_list_data)

        result = read_transactions(file_path)

        self.assertEqual(result, empty_list_data)
        mock_os_exists.assert_called_once_with(file_path)
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_not_a_list(self, mock_file_open, mock_os_exists):
        """
        Тестируем чтение файла, который содержит JSON, но не является списком.
        """
        file_path = "../data/operations.json"
        not_a_list_json = {"transaction_id": 123, "value": 500}

        mock_os_exists.return_value = True
        mock_file_open.return_value.read.return_value = json.dumps(not_a_list_json)

        result = read_transactions(file_path)

        self.assertEqual(result, [])
        mock_os_exists.assert_called_once_with(file_path)
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

    # Более точный вариант для file_not_found, без использования assertRaises
    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", side_effect=FileNotFoundError)  # Имитируем, что open выдаст ошибку
    def test_read_transactions_file_not_found_v2(self, mock_file_open, mock_os_exists):
        """
        Альтернативный тест для случая, когда файл не существует.
        """
        file_path = "../data/non_existent_operations.json"

        mock_os_exists.return_value = True  # os.path.exists вернет True, но open будет имитировать ошибку
        # Это не идеальный сценарий, так как логика функции сначала проверяет exists.
        # Давайте исправим наш подход.

    @patch("src.utils.os.path.exists")
    def test_read_transactions_file_not_found_correct(self, mock_os_exists):
        """
        Корректный тест для случая, когда файл не существует.
        """
        file_path = "../data/non_existent_operations.json"

        mock_os_exists.return_value
