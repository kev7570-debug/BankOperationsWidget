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