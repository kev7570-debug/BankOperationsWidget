# Проект "Bank Operations Widget"

## Описание:
Учебный Проект "Bank Operations Widget" представляет собой виджет для просмотра последних операций клиентов банка. 
Виджет сортирует и фильтрует банковские операции по указанным параметрам.

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/kev7570-debug/BankOperationsWidget
```

2. Установка зависимостей:
```
pip install -r requirements.txt
```

## Использование:
#### Фильтрация операций по статусу
```
from src.processing import filter_by_state

transactions = [...]
filtered_tx = filter_by_state(transactions, state="EXECUTED")
```

#### Сортировка операций по дате
```
from src.processing import sort_by_date
sorted_tx = sort_by_date(transactions)
```

##### Тестирование
Добавлены тесты для всех функций проекта. Документация обновлена.

## Изменения
- Добавлены тесты для всех функций.
- Обновлён README-файл с инструкциями по запуску тестов и оценке покрытия.
- Усовершенствована структура тестов с применением фикстур и параметризации.

## Отет о тестировании
Отчёт о покрытии доступен в папке `htmlcov/`.

###### Модуль: Generators
Модуль `Generators` предоставляет инструменты для эффективного анализа большого объёма финансовых транзакций с использованием возможностей Python — генераторов.

#### Функции:
- **filter_by_currency**: фильтрует транзакции по заданной валюте.
- **transaction_descriptions**: генератор, который по запросу возвращает описания транзакций.
- **card_number_g3enerator**: генерирует номера банковских карт в заданном диапазоне.

### Пример использования:
```
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
```

###### Модуль: Decorators 
Модуль `decorators` предоставляет вспомогательную функцию — декоратор `log`, который позволяет регистрировать подробности выполнения функций, включая их аргументы, результаты и возникающие ошибки.

### Использование декоратора:
pythonfrom src.decorators import log
@log(filename="mylog.txt")def my_function(x, y):    return x + y
my_function(1, 2)


## Авторские права:
Автор проекта: Кашина Елена
Год: 2026
