# tests/test_masks.py

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    # Тестирование стандартной карты
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"

    # Тестирование минимальной границы (16-значное число)
    assert get_mask_card_number(1000000000000000) == "1000 00** **** 0000"

    # Тестирование максимальной границы (16-значное число)
    assert get_mask_card_number(9999999999999999) == "9999 99** **** 9999"

    # Тестирование некорректного ввода (меньше 16 знаков)
    try:
        get_mask_card_number(123456789012345)  # 15 знаков
        assert False, "Функция должна выбросить ошибку при недостаточном числе символов!"
    except Exception as e:
        assert isinstance(e, ValueError), "Ошибка должна быть типа ValueError"


def test_get_mask_account():
    # Тестирование стандартного счета
    assert get_mask_account(1234567890123456) == "**3456"

    # Тестирование минимальной границы (16-значное число)
    assert get_mask_account(1000000000000000) == "**0000"

    # Тестирование максимальной границы (16-значное число)
    assert get_mask_account(9999999999999999) == "**9999"

    # Тестирование некорректного ввода (меньше 16 знаков)
    try:
        get_mask_account(123456789012345)  # 15 знаков
        assert False, "Функция должна выбросить ошибку при недостаточном числе символов!"
    except Exception as e:
        assert isinstance(e, ValueError), "Ошибка должна быть типа ValueError"
