# api_yamdb

Проект YaMDb собирает отзывы пользователей на различные произведения.

## **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

>*git clone https://github.com/airatns/api_final_yatube.git*

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
