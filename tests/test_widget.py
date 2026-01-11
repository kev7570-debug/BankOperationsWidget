# tests/test_widget.py

from src.widget import mask_account_card, get_date

def test_mask_account_card():
    # Тестирование карты
    visa = "Visa Platinum 7000792289606361"
    maestro = "Maestro 7000792289606361"
    account = "Счет 73654108430135874305"

    # Проверка, что для карты Visa результат корректен
    assert mask_account_card(visa) == "Visa Platinum 7000 79** **** 6361"

    # Проверка, что для карты Maestro результат корректен
    assert mask_account_card(maestro) == "Maestro 7000 79** **** 6361"

    # Проверка, что для счета результат корректен
    assert mask_account_card(account) == "Счет **4305"

def test_get_date():
    # Тестирование преобразования даты
    iso_date = "2023-04-15T12:34:56.789012"
    expected_date = "15.04.2023"

    # Проверка корректности преобразования даты
    assert get_date(iso_date) == expected_date


