# YaMDb

YaMDb - это проект, который собирает отзывы пользователей на произведения.

Произведения делятся на категории: **"Книги"**, **"Фильмы"**, **"Музыка"**. Список категорий может быть расширен администратором.

Пользователи оставляют текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти. Из усредненных оценок формируется **рейтинг**.

## **Стек технологий**

Python, Django, Django REST Framework, Simple JWT, SQLite3

## **Техническое описание проекта**

Написаны бэкенд проекта и API для него.

Модель **User** переопределена.

База данных наполнена контентом из **csv**-файлов. 

## **Пользовательские роли:**

* **Аноним**: может читать отзывы и комментарии, просматривать описания произведений

* **Аутентифицированный пользователь**: может публиковать свои отзывы, комментировать чужие отзывы, ставить оценки произведениям.

* **Модератор**: может удалять и редактировать любые отзывы и комментарии.

* **Администратор**: может создавать и удалять произведения, категории и жанры, назначать роли пользователям.

* **Суперюзер Django**: полные права на управление всем проектом.

## **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

>*git clone https://github.com/airatns/api_yamdb*

Cоздать и активировать виртуальное окружение:

>*python3 -m venv env*

>*source env/scripts/activate*

Установить зависимости из файла requirements.txt:

>*python3 -m pip install --upgrade pip*

>*pip install -r requirements.txt*

Выполнить миграции:

>*python3 manage.py migrate*

Запустить проект:

>*python3 manage.py runserver*

## **Регистрация нового пользователя**
>*http://127.0.0.1:8000/api/v1/auth/signup/*

Для регистрации введите **email** и **username**.

Затем на ваш электронный почтвый ящик придёт **confirmation_code**.

## **Получение JWT-токена**
>*http://127.0.0.1:8000/api/v1/auth/token/*

Для аутентификации введите **username** и **confirmation_code**.

Вам будет выдан **token** для запросов к API.

Срок действия токена **14 дней**.

### **Пример использования JWY-токена**

>*Bearer ey8Df...*


## **Примеры запросов к API**

### **Изменение данных своей учетной записи**

>*http://127.0.0.1:8000/api/v1/users/me/*

*Request*

>*"first_name": "first",*

>*"last_name": "forever"*

>*"bio": "I was born on January 1st"*

*Response*

>*"username": "first#1",*

>*"email": "first#1@google.com",*

>*"first_name": "first",*

>*"last_name": "forever"*

>*"bio": "I was born on January 1st"*

>*"role": "user"*

### **Удаление жанра**

>*DELETE /api/v1/genres/{slug}/*

*Response*

>*HTTP Code: 204*

### **Добавление произведения**

>*POST /api/v1/titles/*

*Request*
>{
>
>*"name": "Alien",*
> 
>*"year": 1979*
>
>*"description": "In space no one can hear your scream"*
>
>*"genre": "horror"*
>
>*"category": "films"*
>
>}


*Response*
>{
> 
>*"id": 13,*
>
>*"name": "Alien",*
>
>*"year": 1979*
>
>*"rating": "None"*
>
>*"description": "In space no one can hear your scream"*
>
>*"genre"*: 
> [{
> *"slug": "horror"*,
> *"name": "Ужасы"*
> }]
>
>*"category"*: {
> *"slug"*: *"films"*,
> *"name"*: *"Кино"*
> }
>
> }
