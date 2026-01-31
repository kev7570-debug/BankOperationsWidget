import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def convert_to_rubles(transaction):
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    params = {'symbols': 'RUB', 'base': currency}
    headers = {'apikey': API_KEY}

    try:
        response = requests.get(
            base_url,
            params=params,
            headers=headers
        )
        response.raise_for_status()  # Проверяем успешность запроса

        data = response.json()
        exchange_rate = data['rates']['RUB']
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)
    except requests.exceptions.HTTPError as errh:
        print(
            f"HTTP Error occurred ({response.status_code}): "
            f"{response.text}"
        )
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error occurred: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
    except requests.exceptions.RequestException as err:
        print(
            f"An unknown error occurred: {err}. "
            f"Response text: {getattr(response, 'text', '')}"
        )
    return None


# if __name__ == "__main__":
#     Пример транзакции в долларах США
#     example_transaction = {
#         'operationAmount': {
#             'amount': '100',
#             'currency': {'code': 'USD'}
#         }
#     }

    # Конвертируем сумму в рубли
    # result = convert_to_rubles(example_transaction)
    # print(f"Сумма в рублях: {result}")
