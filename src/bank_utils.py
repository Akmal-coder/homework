import re
import json
import csv
from typing import List, Dict, Any
from collections import Counter
from openpyxl import load_workbook


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список данных по наличию заданного поискового шаблона в поле 'description'.

    Проводит поиск с учетом регистра (игнорируя регистр символов).

    """
    pattern = re.compile(search, re.IGNORECASE)
    filtered_items = [item for item in data if pattern.search(item.get("description", ""))]
    return filtered_items


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций, соответствующих каждой категории.

    Категории — список строк, и поиск в описании осуществляется по вхождению подстроки (игнорируя регистр).

    """
    counts = Counter()
    lower_categories = [c.lower() for c in categories]

    for item in data:
        desc = item.get("description", "").lower()
        for cat_lower, cat_orig in zip(lower_categories, categories):
            if cat_lower in desc:
                counts[cat_orig] += 1
                break
    return dict(counts)


def load_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список данных из JSON-файла.

    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список данных из CSV-файла.

    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_xlsx(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список данных из XLSX-файла.

    Читает активный лист книги, первую строку использует как заголовки,
    остальные — как строки с данными.

    """
    wb = load_workbook(file_path)
    ws = wb.active
    rows = ws.rows
    headers = [cell.value for cell in next(rows)]
    data = []
    for row in rows:
        item = {}
        for header, cell in zip(headers, row):
            item[header] = cell.value
        data.append(item)
    return data
