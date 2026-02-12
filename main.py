# from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
#
# # Пример данных для тестирования
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {
#             "amount": "43318.34",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160"
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {
#             "amount": "56883.54",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229"
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {
#             "amount": "67314.70",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657"
#     }
# ]
#
# # Тестирование функции filter_by_currency
# print("Тест функции filter_by_currency:")
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(3):
#     print(next(usd_transactions))
#
# # Тестирование функции transaction_descriptions
# print("\nТест функции transaction_descriptions:")
# descriptions = transaction_descriptions(transactions)
# for _ in range(len(transactions)):
#     print(next(descriptions))
#
# # Тестирование функции card_number_generator
# print("\nТест функции card_number_generator:")
# for card_number in card_number_generator(1, 5):
#     print(card_number)


# from src.decorators import log
#
# # Демонстрация использования декоратора log
# @log(filename="example.log")
# def example_function(x, y):
#     return x + y
#
# # Вызов декорированной функции
# example_function(1, 2)
#
# # Демонстрация обработки ошибки
# @log(filename="example.log")
# def error_function(x, y):
#     raise ValueError("This is an error.")
#
# try:
#     error_function(3, 4)
# except ValueError:
#     pass  # Игнорируем ошибку для демонстрационного примера


# from src.data_reader import read_csv, read_excel
#
# # Пример вызова функций
# csv_file_path = r'C:\Users\User\PycharmProjects\Domashka\data\transactions.csv'
# excel_file_path = r'C:\Users\User\PycharmProjects\Domashka\data\transactions_excel.xlsx'
#
# # Чтение CSV-файла
# csv_transactions = read_csv(csv_file_path)
# print("Транзакции из CSV:", csv_transactions)
#
# # Чтение Excel-файла
# excel_transactions = read_excel(excel_file_path)
# print("Транзакции из Excel:", excel_transactions)



# src/main.py

from src.data_reader import read_csv, read_excel, read_json
from src.search import process_bank_search
from src.statistics import process_bank_operations


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")
    if choice == '1':
        data = read_json('./data/operations.json')
    elif choice == '2':
        data = read_csv('./data/transactions.csv')
    elif choice == '3':
        data = read_excel('./data/transactions_excel.xlsx')
    else:
        print("Недопустимый выбор.")
        return

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status_choice = input("Введите статус операций для фильтрации (EXECUTED/CANCELED/PENDING): ").upper()
        if status_choice in valid_statuses:
            break
        else:
            print(f"Статус операции \"{status_choice}\" недоступен.")

    # Применяем фильтр по статусу
    filtered_data = [txn for txn in data if str(txn.get('state', '')).upper() == status_choice]

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").lower()
    if sort_choice == 'да':
        ascending_choice = input("Сортировать по возрастанию или по убыванию? (Возрастание/Убывание): ").lower()
        filtered_data.sort(key=lambda x: x['date'], reverse=(ascending_choice == 'убывание'))

    # Фильтрация по валюте
    currency_choice = input("Выводить только рублевые транзакции? (Да/Нет): ").lower()
    if currency_choice == 'да':
        filtered_data = [
            txn for txn in filtered_data
            if txn.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB'
        ]

    # Поиск по словам в описании
    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").lower()
    if search_choice == 'да':
        search_term = input("Введите слово для поиска: ")
        filtered_data = process_bank_search(filtered_data, search_term)

    # Вывод итогового списка операций
    print("Итоговый список транзакций:")
    if filtered_data:
        for idx, txn in enumerate(filtered_data):
            amount = txn.get('operationAmount', {}).get('amount', 'N/A')
            currency = txn.get('operationAmount', {}).get('currency', {}).get('name', 'N/A')
            print(
                f"{idx + 1}. Дата: {txn.get('date', '')}, Сумма: {amount} {currency}, "
                f"Описание: {txn.get('description', '')}"
            )
    else:
        print("Не найдено ни одной транзакции, соответствующей условиям фильтрации.")


if __name__ == '__main__':
    main()
