# convert_valut
Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
Ответ:
{

"result": 62.16

}
Любой фреймворк в пределах python.
Данные о текущих курсах валют необходимо получать с внешнего сервиса.
Контейнерезация, документация, и прочее — приветствуется.