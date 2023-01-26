# YATUBE(API)
_________________________________________________
## Описание
Социальная сеть для публикации личных дневников

[![N|Solid](https://ie.wampi.ru/2022/10/15/logoza.ru.png)](https://ie.wampi.ru)

### YATUBE - социальная сеть, в которой Вы можете:

- Создать свою собственную страницу для публикации своих записей
- Заходить на чужие страницы, подписываться на авторов и комментировать их записи
- Делиться записями в сообществах
- Обладает удобным API-интерфейсом
 
_____________________________________________________

## Техническое описание

### Примененные технологии
 > Python 3.7.9
 > Django 3.2.16
 > djangorestframework 3.12.4
 > djangorestframework-simplejwt 4.7.2
 > PyJWT 2.1.0

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/cra1ger/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры запросов
### Создание поста
>Тип запроса 
```POST```
>Endpoint 
```api/v1/posts/```

Запрос:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
______________________________________
### Авторы
Даниил Алексеенко

### Лицензия
BSD 3-Clause License
