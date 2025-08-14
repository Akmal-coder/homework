from datetime import datetime


def filter_by_state(list_dict: list, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению."""
    filter_list = []  # Создаем пустой список для результатов
    for dict_item in list_dict:  # Перебираем все элементы входного списка
        if dict_item.get("state") == state:  # Проверяем ключ 'state'
            filter_list.append(dict_item)  # Добавляем подходящий словарь в результат
    return filter_list


if __name__ == "__main__":
    result = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
    print(result)
