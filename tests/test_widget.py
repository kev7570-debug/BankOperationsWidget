# tests/test_widget.py

import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def transaction_data():
    return {
        "visa": "Visa Platinum 7000792289606361",
        "maestro": "Maestro 7000792289606361",
        "account": "Счет 73654108430135874305"
    }

@pytest.mark.parametrize("data_type, expected_output", [
    ("visa", "Visa Platinum 7000 79** **** 6361"),
    ("maestro", "Maestro 7000 79** **** 6361"),
    ("account", "Счет **4305")
])
def test_mask_account_card(transaction_data, data_type, expected_output):
    input_value = transaction_data[data_type]
    result = mask_account_card(input_value)
    assert result == expected_output

@pytest.mark.parametrize("input_value, expected_output", [
    ("2023-01-01T12:00:00Z", "01.01.2023"),
    ("", ""),
    ("invalid_format", "")
])
def test_get_date(input_value, expected_output):
    result = get_date(input_value)
    assert result == expected_output
