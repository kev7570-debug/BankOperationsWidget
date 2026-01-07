# tests/test_processing.py

import pytest
from src.processing import filter_by_state, sort_by_date
from datetime import datetime

@pytest.fixture
def sample_transactions():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
        {'id': 4, 'state': 'PENDING', 'date': '2023-01-04'}
    ]

@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),
    ("CANCELED", [2]),
    ("PENDING", [4]),
    ("UNKNOWN", [])
])
def test_filter_by_state(sample_transactions, state, expected_ids):
    result = filter_by_state(sample_transactions, state)
    ids = [item['id'] for item in result]
    assert ids == expected_ids

@pytest.mark.parametrize("reverse, expected_order", [
    (False, ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
    (True, ['2023-01-04', '2023-01-03', '2023-01-02', '2023-01-01'])
])
def test_sort_by_date(sample_transactions, reverse, expected_order):
    result = sort_by_date(sample_transactions, reverse=reverse)
    dates = [datetime.strptime(item['date'], '%Y-%m-%d').strftime('%Y-%m-%d') for item in result]
    assert dates == expected_order


