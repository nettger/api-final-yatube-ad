# API для Yatube

## Описание проекта

API для социальной сети Yatube.  
Проект предоставляет возможность работать с публикациями, комментариями, группами и подписками через REST API.

Функциональность:
- получение списка публикаций и отдельной публикации;
- создание, редактирование и удаление собственных публикаций;
- работа с комментариями;
- просмотр групп;
- подписка на авторов;
- аутентификация пользователей с помощью JWT-токенов.

Неаутентифицированные пользователи имеют доступ только на чтение.  
Аутентифицированные пользователи могут создавать и изменять собственный контент.

## Технологии

- Python 3.10
- Django 3.2
- Django REST Framework
- Simple JWT

## Установка и запуск проекта

Клонировать репозиторий:

git clone https://github.com/your_username/api-final-yatube-ad.git  
cd api-final-yatube-ad  

Перейти в папку с проектом:

cd yatube_api  

Создать и активировать виртуальное окружение:

python3 -m venv venv  
source venv/bin/activate  

Установить зависимости:

pip install -r ../requirements.txt  

Применить миграции:

python manage.py migrate  

Запустить проект:

python manage.py runserver  

Документация API доступна по адресу:

http://127.0.0.1:8000/redoc/

## Аутентификация

В проекте используется JWT-аутентификация.

Получить токен:

POST /api/v1/jwt/create/

Пример запроса:

{
  "username": "your_username",
  "password": "your_password"
}

Пример ответа:

{
  "refresh": "string",
  "access": "string"
}

Для доступа к защищённым эндпоинтам необходимо передавать токен в заголовке:

Authorization: Bearer <access_token>

## Примеры запросов

Получить список публикаций:

GET /api/v1/posts/

Пример ответа:

[
  {
    "id": 1,
    "text": "Текст публикации",
    "author": "username",
    "image": null,
    "group": null,
    "pub_date": "2026-04-17T12:00:00Z"
  }
]

Создать публикацию:

POST /api/v1/posts/

{
  "text": "Новая публикация",
  "group": null
}

Получить комментарии к публикации:

GET /api/v1/posts/{post_id}/comments/

Создать комментарий:

POST /api/v1/posts/{post_id}/comments/

{
  "text": "Новый комментарий"
}

Подписаться на пользователя:

POST /api/v1/follow/

{
  "following": "username"
}

## Автор

Анна Герман