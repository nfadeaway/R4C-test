# Тестовое "R4C - Robots for consumers"

[Легенда](legend.md)

[Таски](tasks.md)

## О решении

#### Общее

- Созданы и загружены `fixtures` для быстрого прогона.

- Переменные окружения в файле `.env.dev`. В рамках тестового SECRET_KEY оставил. Данный файл выложен в Github в рамках тестового.

- Для email-рассылки необходимо заполнить настройки для конкретного сервера в файле `.env.dev`:
```
EMAIL_HOST='smtp.domain.ru'
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST_USER='user@domain.ru'
EMAIL_HOST_PASSWORD='password'
```

- На каждую таску создан PR, все влиты в master.


#### Task 1
`POST`- запрос на ендпоинт `robots/add`

Структура запроса:
```
{
  "model": "M1",
  "version": "N1",
  "created": "2023-09-28 03:59:59"
}
```
Валидация входящего JSON реализована с помощью библиотеки `jsonschema`.

#### Task 2

`GET`- запрос на ендпоинт `robots/week-factory-report`.

Отчет формируется в папке `reports` в формате `xlsx` за последнюю завершенную неделю с разбивкой согласно ТЗ.

#### Task 3

Создан сигнал на добавление робота в базу. Если вновь добавленная модель находится в ордерах, то соответствующим клиентам отправляется уведомление на указанный email.
Для рассылки используются стандартные средства Django. Необходимо лишь заполнить соответствующие настройки сервера в файле `.env.dev`.