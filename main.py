from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    # Тестирование функции маскировки номера карты
    card_number = 7000792289606361
    masked_card = get_mask_card_number(card_number)
    print(f"Маскировка карты: {masked_card}")  # Ожидаемый результат: 7000 79** **** 6361

    # Тестирование функции маскировки счета
    account_number = 73654108430135874305
    masked_account = get_mask_account(account_number)
    print(f"Маскировка счета: {masked_account}")  # Ожидаемый результат: **4305

    # ТЕСТИРОВАНИЕ НОВЫХ ФУНКЦИЙ
    print("===> Тест новой функции mask_account_card:")
    test_cases_mask = [
        ('Visa Platinum 7000792289606361',
         'Visa Platinum 7000 79** **** 6361'),  # Строка сокращена
        ('Maestro 7000792289606361',
         'Maestro 7000 79** **** 6361'),       # Строка сокращена
        ('Счет 73654108430135874305',
         'Счет **4305'),                        # Строка сокращена
    ]

    for case_input, expected_output in test_cases_mask:
        actual_result = mask_account_card(case_input)
        assert actual_result == expected_output, (
            f"Test failed for '{case_input}'. Expected: {expected_output}, "
            f"Got: {actual_result}"
        )
        print(f"Тест OK: '{case_input}' -> '{actual_result}'")

    # Тестируем преобразование даты
    test_case_get_date = (
        "2024-03-11T02:26:18.671407",
        "11.03.2024"
    )

    converted_date = get_date(test_case_get_date[0])
    assert converted_date == test_case_get_date[1], (
        f"Test failed for '{test_case_get_date[0]}'. Expected: {test_case_get_date[1]}, "
        f"Got: {converted_date}"
    )
    print(f"Тест OK: '{test_case_get_date[0]}' -> '{converted_date}'")
