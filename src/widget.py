import re  # Необходимый модуль для регулярного выражения
from datetime import datetime
from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Получает строку с типом карты/счета и номером и возвращает замаскированную версию"""
    parts = input_string.rsplit(None, 1)

    if len(parts) != 2:
        raise ValueError("Неправильно сформирована входная строка")

    type_name, raw_number = parts

    # Извлекаем чистое число из строки с помощью регулярного выражения
    match = re.search(r'\b\d+\b', raw_number)
    if not match:
        raise ValueError("Невозможно распознать номер")

    number = match.group()  # извлекаем чистое число
    try:
        number_int = int(number)
    except ValueError:
        raise ValueError("Неверный формат номера")

    if "счет" in type_name.lower():
        return f"{type_name} {get_mask_account(number_int)}"
    else:
        return f"{type_name} {get_mask_card_number(number_int)}"


def get_mask_account(account_number: int) -> str:
    """Функция возвращает замаскированный банковский счет"""
    last_four_digits = f"{account_number % 10000:04d}"
    return f"**{last_four_digits}"


def get_date(date_string: str) -> str:
    """Преобразует дату в формат дд.мм.гггг"""
    dt = datetime.fromisoformat(date_string[:-7])  # отрезание микросекунд
    return dt.strftime("%d.%m.%Y")
