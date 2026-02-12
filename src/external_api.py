import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def convert_to_rubles(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции
    :return: Сумма транзакции в рублях (float)
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    # Новый URL для конвертации валюты
    base_url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        'to': 'RUB',
        'from': currency,
        'amount': amount
    }
    headers = {'apikey': API_KEY}

    try:
        response = requests.get(
            base_url,
            params=params,
            headers=headers
        )
        response.raise_for_status()  # Проверяем успешность запроса

        data = response.json()
        converted_amount = data['result']
        return round(float(converted_amount), 2)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error occurred ({response.status_code}): {response.text}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error occurred: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unknown error occurred: {err}. Response text: {getattr(response, 'text', '')}")
    return None


# пример вызова функции
example_transaction = {
    'operationAmount': {
        'amount': '100',
        'currency': {'code': 'USD'}
    }
}

result = convert_to_rubles(example_transaction)
print(f"Сумма в рублях: {result}")
