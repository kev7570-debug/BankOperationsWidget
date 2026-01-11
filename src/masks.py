def get_mask_card_number(card_number: int) -> str:
    """Функция возвращает замаскированный номер банковской карты"""
    if len(str(card_number)) != 16:
        raise ValueError("Длина номера карты должна составлять ровно 16 символов!")

    card_number_str = f"{card_number:016d}"  # приводим к строке длиной в 16 символов
    first_block = card_number_str[:4]  # первые четыре цифры
    second_block = card_number_str[4:6] + "**"  # вторые две цифры плюс **
    third_block = "****"  # третья группа звездочек
    fourth_block = card_number_str[-4:]  # последние 4 цифры
    return f"{first_block} {second_block} {third_block} {fourth_block}"


def get_mask_account(account_number: int) -> str:
    """Функция возвращает замаскированный банковский счет"""
    if len(str(account_number)) != 16:
        raise ValueError("Длина номера счета должна составлять ровно 16 символов!")

    last_four_digits = f"{account_number % 10000:04d}"
    return f"**{last_four_digits}"
