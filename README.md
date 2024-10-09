# RestfulAPI

## Задача

Необходимо создать RESTful API сервис, позволяющий управлять списком
кинофильмов

## Методы

### GET Методы

1. `/api/movies` - список всех кинофильмов.

Необходимо возвратить ответ с кодом 200 (OK) и вложить JSON следующей
структуры:

```json
{
  "list": [
    {
      "id": 1,
      "title": "Example movie",
      "year": 2018,
      "director": "Somebody",
      "length": "02:30:00",
      "rating": 8
    }
  ]
}
```

1. `/api/movies/:id` - информация о кинофильме с указанным id.

Необходимо возвратить ответ с кодом 200 (OK) и вложить JSON следующей
структуры:

```json
{
    "movie": {
        "id": 1,
        "title": "Example movie",
        REST-full API 2
        "year": 2018,
        "director": "Somebody",
        "length": "02:30:00",
        "rating": 8
    }
}
```

В случае, если записи с указанным id не найдено, необходимо возвратить ответ с
кодом 404 (Not Found)

### POST Методы

1. `/api/movies` - добавление новой записи о кинофильме.

В теле входящего запроса необходимо ожидать JSON следующей структуры:

```json
{
"movie": {
        "id": 1,
        "title": "Example movie",
        "year": 2018,
        "director": "Somebody",
        "length": "02:30:00",
        "rating": 8
    }
}
```

В случае успешного добавления в список необходимо возвратить ответ с кодом
200 (OK) и вложить JSON следующей структуры:

```json
{
    "movie": {
        "id": <уникальный идентификатор записи>,
        "title": "Example movie",
        "year": 2018,
        "director": "Somebody",
        REST-full API 3
        "length": "02:30:00",
        "rating": 8
    }
}
```

В случае неудачи необходимо возвратить ответ с кодом 500 (Internal Server Error) и
вложить JSON следующей структуры:

```json
{
    "status": 500,
    "reason": "<Причина неудачи>"
}
```

### PATCH Методы

1. `/api/movies/:id` - изменение информации о кинофильме с указанным id.

Входящий запрос и формат ответов при удачном и неудачном изменении
совпадают с предыдущим методом
в случае, если записи с указанным id не найдено, необходимо возвратить ответ с
кодом 404 (Not Found)

### DELETE Методы

1. `/api/movies/:id` - удаление записи с указанным id.

В случае успеха необходимо возвратить ответ с кодом 202 (Accepted)
в случае, если записи с указанным id не найдено, необходимо возвратить ответ с
кодом 404 (Not Found)
в случае других ошибок необходимо возвратить ответ с кодом 500 (Internal Server
Error) и вложить JSON следующей структуры:

```json
{
    "status": 500,
    "reason": "<Причина неудачи>"
}
```

## Запись о кинофильме

Запись о кинофильме имеет следующие поля (все поля обязательны для
заполнения):

1. `id` - целочисленный уникальный идентификатор записи
REST-full API 4
2. `title` - название кинофильма, строка до 100 символов
3. `year` - год выпуска, целое число от 1900 до 2100;
4. `director` - ФИО режиссера, строка до 100 символов;
5. `length` - продолжительность фильма, тип - время;
6. `rating` - рейтинг фильма (целое число от 0 до 10).

Необходимо валидировать входящие значения полей при создании и изменении
записи.
В случае ошибки валидации необходимо сформировать ответ с кодом 400 (Bad
Request), в теле ответа указать причину ошибки валидации.
Пример ответа на попытку вставить запись без указания названия кинофильма:

```json
{
    "status": 400,
    "reason": "Field 'title' is required"
}
```

Пример ответа на попытку вставить запись с годом, превышающим максимально
допустимое значение:

```json
{
    "status": 400,
    "reason": "Field 'year' should be less then 2100"
}
```
