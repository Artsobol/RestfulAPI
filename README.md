# RestfulAPI

## Описание проекта

Необходимо создать RESTful API сервис, позволяющий управлять списком
кинофильмов

RestfulAPI — это сервис для управления списком кинофильмов. С помощью API можно добавлять, изменять, удалять и получать информацию о фильмах.

## Технологии
- Python 3.12
- FastAPI 
- PostgreSQL 17
- Docker
- Nginx
- Gunicorn

## Методы API
- `GET /api/movies` - Получение списка всех фильмов
- `GET /api/movies/:id` - Получение информации о конкретном фильме
- `POST /api/movies` - Добавление нового фильма
- `PATCH /api/movies/:id` - Обновление информации о фильме
- `DELETE /api/movies/:id` - Удаление фильма

Полная документация API доступна [здесь](./API_DOCUMENTAION.md).

## Установка и запуск

### 1. Клонирование репозитория

Сначала склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/Artsobol/RestfulAPI.git
cd RestfulAPI
```

### Запуск с помощью Docker

1. **Создание образа**

   Для запуска с помощью Docker запустите его и введите следующую команду в терминале:
   
   ```bash
   docker compose -f docker-compose.prod.yml up -d --build
   ```

2. **Миграции**

   Примените миграции, выполнив следующую команду:
   
   ```bash
   docker compose -f docker-compose.prod.yml exec web alembic upgrade head
   ```

### Запуск без Docker

1. **Настройка базы данных**

   Установите PostgreSQL и создайте базу данных, пользователя и пароль. Откройте файл `db.py` в папке `app/backend` и замените строку подключения к базе данных на ваши данные:

   ```
   engine = create_async_engine('postgresql+asyncpg://postgres_user:postgres_password@localhost:5432/postgres_database', 
                                echo=True)
   ```

   Обратите внимание, что хост (вместо `db`) нужно указать как `localhost`, если вы запускаете без Docker.

2. **Настройка Alembic**

   Откройте файл `alembic.ini` и измените строку подключения к базе данных, чтобы она соответствовала вашим настройкам:

   ```ini
   sqlalchemy.url = postgresql+asyncpg://postgres_user:postgres_password@localhost:5432/postgres_database
   ```

3. **Применение миграций**

   Выполните миграции для создания таблиц в базе данных. Это можно сделать с помощью следующих команд:

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

4. **Запуск приложения**

   Запустите приложение с помощью команды:

   ```bash
   uvicorn app.main:app --reload
   ```

   Приложение будет доступно по адресу `http://localhost:8000`

## TODO

   1. Убрать ручной ввод ID при создании фильма
   2. Добавить сущность режиссера, как отдельную таблицу. Сделать связь One to Many
   3. Добавить сущность пользователей, сделать авторизацию
   4. Расширить таблицу с фильмами
   
