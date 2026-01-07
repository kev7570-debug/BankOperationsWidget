from typing import List, Dict, Union


def filter_by_state(
        transactions: List[Dict[str, Union[int, str]]],
        state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str]]]:
    """ Фильтрация списка операций по состоянию """
    filtered_transactions = [tx for tx in transactions if tx.get("state") == state]
    return filtered_transactions


from datetime import datetime


def sort_by_date(
        transactions: List[Dict[str, Union[int, str]]],
        reverse: bool = True
) -> List[Dict[str, Union[int, str]]]:
    """ Сортировка списка операций по дате"""
    sorted_transactions = sorted(
        transactions,
        key=lambda tx: datetime.strptime(tx["date"], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=reverse
    )
    return sorted_transactions
