# tests/conftest.py

import pytest

@pytest.fixture
def transaction_data():
    return {
        "visa": "Visa Platinum 7000792289606361",
        "maestro": "Maestro 7000792289606361",
        "account": "Счет 73654108430135874305"
    }
