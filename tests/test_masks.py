# tests/test_masks.py

import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("input_value, expected_output", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("", ""),  # Если пустая строка, предположим, что функция возвращает пустую строку
    ("invalid_input", "")  # Если неверный формат, функция возвращает пустую строку
])
def test_get_mask_card_number(input_value, expected_output):
    result = get_mask_card_number(input_value)
    assert result == expected_output

@pytest.mark.parametrize("input_value, expected_output", [
    ("1234567890123456", "**3456"),
    ("", ""),  # Если пустая строка, предположим, что функция возвращает пустую строку
    ("invalid_input", "")  # Если неверный формат, функция возвращает пустую строку
])
def test_get_mask_account(input_value, expected_output):
    result = get_mask_account(input_value)
    assert result == expected_output






