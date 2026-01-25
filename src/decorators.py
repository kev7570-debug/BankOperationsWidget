import functools
import logging
import traceback
from datetime import datetime


def log(filename=None):
    """
    Декора́тор, регистрирующий детали выполнения функции: время вызова, имя функции,
    аргументы, результат выполнения и ошибки.

    Args:
        filename (str, optional): Имя файла, в который будут записываться логи.
        Если не задано, логи выводятся в консоль.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            function_name = func.__name__
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            try:
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                log_message = f"[{timestamp}] Function {function_name}({signature}) returned {result!r}"
                if filename:
                    with open(filename, mode="a", encoding="utf-8") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)

                return result
            except Exception as ex:
                # Логируем ошибку
                error_message = (
                    f"[{timestamp}] Function {function_name}({signature}) raised {ex.__class__.__name__}: {ex}. "
                    f"Inputs: ({args}, {kwargs})"
                )
                if filename:
                    with open(filename, mode="a", encoding="utf-8") as log_file:
                        log_file.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
