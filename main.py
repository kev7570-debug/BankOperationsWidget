from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    # Тестирование функции маскировки номера карты
    card_number = 7000792289606361
    masked_card = get_mask_card_number(card_number)
    print(f"Маскировка карты: {masked_card}") # Ожидаемый результат: 7000 79** **** 6361

    # Тестирование функции маскировки счета
    account_number = 73654108430135874305
    masked_account = get_mask_account(account_number)
    print(f"Маскировка счета: {masked_account}") # Ожидаемый результат: **4305


from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    # ТЕСТИРОВАНИЕ НОВЫХ ФУНКЦИЙ
    print("===> Тест новой функции mask_account_card:")
    test_cases_mask = [
        ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ]

    for case_input, expected_output in test_cases_mask:
        actual_result = mask_account_card(case_input)
        assert actual_result == expected_output, f"Test failed for '{case_input}'. Expected: {expected_output}, Got: {actual_result}"
        print(f"Тест OK: '{case_input}' -> '{actual_result}'")

    # Тестируем преобразование даты
    test_case_get_date = (
        "2024-03-11T02:26:18.671407",
        "11.03.2024"
    )

    converted_date = get_date(test_case_get_date[0])
    assert converted_date == test_case_get_date[1], f"Test failed for '{test_case_get_date[0]}'. Expected: {test_case_get_date[1]}, Got: {converted_date}"
    print(f"Тест OK: '{test_case_get_date[0]}' -> '{converted_date}'")



from src.processing import filter_by_state, sort_by_date

# Тестовые данные
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Тестирование функции filter_by_state
executed_transactions = filter_by_state(transactions)
canceled_transactions = filter_by_state(transactions, state="CANCELED")

print("Фильтрованные выполненные операции:", executed_transactions)
print("Фильтрованные отмененные операции:", canceled_transactions)

# Тестирование функции sort_by_date
sorted_transactions = sort_by_date(transactions)
ascending_sorted_transactions = sort_by_date(transactions, reverse=False)

print("Отсортированные операции по убыванию:", sorted_transactions)
print("Отсортированные операции по возрастанию:", ascending_sorted_transactions)





