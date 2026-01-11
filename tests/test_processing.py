# tests/test_processing.py

from src.processing import filter_by_state, sort_by_date
from datetime import datetime

def test_filter_by_state():
    # Данные для тестирования
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-15T12:00:00.000"},
        {"id": 2, "state": "CANCELLED", "date": "2023-04-16T12:00:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-04-17T12:00:00.000"}
    ]

    # Проверка фильтрации по состоянию EXECUTED
    result = filter_by_state(transactions)
    assert len(result) == 2
    assert all(tx["state"] == "EXECUTED" for tx in result)

    # Проверка фильтрации по состоянию CANCELLED
    result = filter_by_state(transactions, state="CANCELLED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELLED"

def test_sort_by_date():
    # Данные для тестирования (исправленный формат даты)
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-15T12:00:00.000"},
        {"id": 2, "state": "CANCELLED", "date": "2023-04-16T12:00:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-04-17T12:00:00.000"}
    ]

    # Проверка сортировки по дате в обратном порядке
    result = sort_by_date(transactions)
    assert result[0]["date"] == "2023-04-17T12:00:00.000"
    assert result[-1]["date"] == "2023-04-15T12:00:00.000"

    # Проверка сортировки по дате в прямом порядке
    result = sort_by_date(transactions, reverse=False)
    assert result[0]["date"] == "2023-04-15T12:00:00.000"
    assert result[-1]["date"] == "2023-04-17T12:00:00.000"



