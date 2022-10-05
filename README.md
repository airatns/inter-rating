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

Полное описание можно найти по ссылке после запуска проекта - <a href="http://127.0.0.1:8000/redoc" target="_blank">Redoc</a>

## **Пользовательские роли:**

* **Аноним**: может читать отзывы и комментарии, просматривать описания произведений

* **Аутентифицированный пользователь**: может публиковать свои отзывы, комментировать чужие отзывы, ставить оценки произведениям.

* **Модератор**: может удалять и редактировать любые отзывы и комментарии.

* **Администратор**: может создавать и удалять произведения, категории и жанры, назначать роли пользователям.

* **Суперюзер Django**: полные права на управление всем проектом.

## **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

>*git clone git@github.com:airatns/api_yamdb.git*

Cоздать и активировать виртуальное окружение:

>*python -m venv env* \
>*source env/scripts/activate*

Установить зависимости из файла requirements.txt:

>*python -m pip install --upgrade pip* \
>*pip install -r requirements.txt*

Выполнить миграции:

>*python manage.py migrate*

Залить данные:

>*python manage.py load_data*

Запустить проект:

>*python manage.py runserver*

## **Регистрация нового пользователя**
Для регистрации введите **email** и **username**.

Затем на ваш электронный почтовый ящик придёт **confirmation_code**.

![code](https://user-images.githubusercontent.com/96816183/182865245-3efea538-0ec7-4d16-b8cc-a2a16c1edff4.png)

## **Получение JWT-токена**
Для аутентификации введите **username** и **confirmation_code**.

Вам будет выдан **token** для запросов к API.

Срок действия токена **14 дней**.

![token](https://user-images.githubusercontent.com/96816183/182865510-7f50333d-cf47-40d5-926d-5bcecbb2081d.png)

### **Пример использования JWT-токена**

>*Bearer ey8Df...*


## **Примеры запросов к API**

### **Изменение данных своей учетной записи**

![bio](https://user-images.githubusercontent.com/96816183/182865718-c9ba2d37-d00f-4a6f-8ecd-eb06a9376adc.png)

### **Удаление жанра**

![delete](https://user-images.githubusercontent.com/96816183/182865799-c96ff4d1-be79-4d89-ac7f-2f440c695f8b.png)

### **Добавление произведения**

![title](https://user-images.githubusercontent.com/96816183/182866123-b80f1a88-dbd5-497b-bb0d-4248252db3d9.png)
