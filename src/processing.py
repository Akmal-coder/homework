from datetime import datetime


def filter_by_state(list_dict: list, state="EXECUTED") -> list:
    """Фильтрует список словарей по значению ключа 'state'."""
    filter_list = []
    for dict_item in list_dict:
        if dict_item.get("state") == state:
            filter_list.append(dict_item)
    return filter_list


def sort_by_date_descending(list_dict: list, reverse=True) -> list:
    """Сортирует список словарей по дате.

    Args:
        list_dict (list): список словарей с ключом 'date'.
        reverse (bool): если True, сортирует по убыванию; если False — по возрастанию.

    Returns:
        list: отсортированный список.
    """
    return sorted(
        list_dict,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )


if __name__ == "__main__":
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # Фильтруем по статусу
    filtered = filter_by_state(data, "EXECUTED")
    print("Отфильтрованные по статусу (EXECUTED):")
    for item in filtered:
        print(item)

    # Сортируем по дате (по убыванию)
    sorted_desc = sort_by_date_descending(filtered)
    print("\nОтсортированные по дате (по убыванию):")
    for item in sorted_desc:
        print(item)

    # Сортируем по дате (по возрастанию)
    sorted_asc = sort_by_date_descending(filtered, reverse=False)
    print("\nОтсортированные по дате (по возрастанию):")
    for item in sorted_asc:
        print(item)