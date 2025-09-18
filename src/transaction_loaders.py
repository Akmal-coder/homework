from typing import List, Dict
import pandas as pd
import os


def read_transactions_csv(path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    """
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def read_transactions_excel(path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    """
    df = pd.read_excel(path)
    return df.to_dict(orient="records")


# --- Ниже код, который выполняется сразу при запуске скрипта ---

# Определяем абсолютный путь к текущей папке файла
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(base_dir, "..", "data"))

csv_path = os.path.join(data_dir, "transactions.csv")
excel_path = os.path.join(data_dir, "transactions_excel.xlsx")

# Чтение и вывод транзакций из CSV
try:
    transactions_csv = read_transactions_csv(csv_path)
    print("Транзакции из CSV:")
    for t in transactions_csv:
        print(t)
except FileNotFoundError:
    print(f"Файл CSV не найден по пути: {csv_path}")

print("\n" + "-" * 40 + "\n")

# Чтение и вывод транзакций из Excel
try:
    transactions_excel = read_transactions_excel(excel_path)
    print("Транзакции из Excel:")
    for t in transactions_excel:
        print(t)
except FileNotFoundError:
    print(f"Файл Excel не найден по пути: {excel_path}")
