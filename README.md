# Сервис "Конвертер валют"
Данные о текущих курсах валют берутся с внешнего сервиса и по запросу выводим необходимые данные.

### Стек:
- Python 3.9
- Django 4.2
- Beautifulsoup 4.12
- Djagno Rest framemork 3.14
- Docker 24.0.2

### Как запустить проект:

После клонирования репозитория, переходим в дериктория где находится Dockerfile, и через терминал запускаем сборку образа

```
docker build -t convert_valut .
```

Теперь нужно запустить контейнер
```
docker run --name convert_valut -it -p 8000:8000 convert_valut
```

Введите в адресную строку браузера, чтобы увидеть результат  
```
http://localhost:8000/api/rates?from=USD&to=RUB&value=1
```

Также доступные валюты для просмотра
```
RUB = Russian Ruble,
USD = US Dollar,
EUR = Euro,
INR = Indian Rupee,
GBP = British Pound,
AUD = Australian Dollar,
CAD = Canadian Dollar,
SGD = Singapore Dollar,
CHF = Swiss Franc,
MYR = Malaysian Ringgit,
JPY = Japanese Yen,
CNY = Chinese Yuan Renminbi,
CZK = Czech Koruna,
TRY = Turkish Lira
```

Посмотреть документацию по API, которая автоматически обновляется при добавлении новых эндпоинтов
```
http://localhost:8000/redoc/
```
или
```
http://localhost:8000/swagger/
```

### Автор проекта:
[Владислав Тутункин](`https://github.com/TutunkinVladislav`)
