import logging
import os  # Добавляем импорт модуля os

# Создаём логгер для модуля masks
logger_masks = logging.getLogger(__name__)
logger_masks.setLevel(logging.DEBUG)

# Создаём обработчик для записи логов в файл
logs_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(logs_folder, exist_ok=True)
log_file_path = os.path.join(logs_folder, 'masks.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Устанавливаем форматер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger_masks.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция возвращает замаскированный номер банковской карты"""
    logger_masks.debug(f"Начало маскировки карты {card_number}")

    if len(str(card_number)) != 16:
        logger_masks.error(f"Ошибка: неверная длина номера карты {card_number}. Ожидалось 16 символов.")
        raise ValueError("Длина номера карты должна составлять ровно 16 символов!")

    card_number_str = f"{card_number:016d}"  # приводим к строке длиной в 16 символов
    first_block = card_number_str[:4]  # первые четыре цифры
    second_block = card_number_str[4:6] + "**"  # вторые две цифры плюс **
    third_block = "****"  # третья группа звездочек
    fourth_block = card_number_str[-4:]  # последние 4 цифры
    masked_card = f"{first_block} {second_block} {third_block} {fourth_block}"

    logger_masks.info(f"Карта {card_number} успешно замаскирована как {masked_card}")
    return masked_card


# Вызов функции
masked_card = get_mask_card_number(1234567890123456)
print(masked_card)


def get_mask_account(account_number: int) -> str:
    """Функция возвращает замаскированный банковский счет"""
    logger_masks.debug(f"Начало маскировки счета {account_number}")

    if len(str(account_number)) != 16:
        logger_masks.error(f"Ошибка: неверная длина номера счета {account_number}. Ожидалось 16 символов.")
        raise ValueError("Длина номера счета должна составлять ровно 16 символов!")

    last_four_digits = f"{account_number % 10000:04d}"
    masked_account = f"**{last_four_digits}"

    logger_masks.info(f"Счет {account_number} успешно замаскирован как {masked_account}")
    return masked_account


# Вызов функции get_mask_account
masked_account = get_mask_account(1234567890123456)
print(masked_account)
