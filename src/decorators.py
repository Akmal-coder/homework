from typing import Callable, Optional, Any
import functools


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функции.

    Логирует успешное выполнение функции или возникшие исключения.
    Логи можно выводить в консоль (по умолчанию) или записывать в файл.

    Args:
        filename (Optional[str]): Путь к файлу для записи логов. Если None, логи выводятся в консоль.

    Returns:
        Callable: Декоратор, который оборачивает функцию с логированием.
    """

    def decorator(func: Callable) -> Callable:
        """
        Обертка-декоратор для функции.

        Args:
            func (Callable): Функция, которую нужно обернуть.

        Returns:
            Callable: Обернутая функция с логированием.
        """

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка, которая выполняет функцию и логирует результат или ошибку.

            Args:
                *args (Any): Позиционные аргументы функции.
                **kwargs (Any): Именованные аргументы функции.

            Returns:
                Any: Результат выполнения функции.

            Raises:
                Exception: Пробрасывает исключения, возникшие внутри функции.
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
