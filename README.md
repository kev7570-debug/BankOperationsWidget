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

## Авторские права:
```
Автор проекта: Кашина Елена
Год: 2025
```



