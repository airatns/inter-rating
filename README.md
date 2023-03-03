# Inter Rating

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;

YaMDb is the community with users reviews of movies, books and music. The backend was developed in Python using Django Rest Framework (API). The User model was updated and extended by additional fields. Also implemented custom authorization and authentication via a JWT. The data was imported to the database from a csv file using Django management command

Works of art are allocated into categories: **"Books"**, **"Movies"**, **"Musical compositions"**. Categories can be expanded by the administrator.

Users leave comments on and rate a work of art in the range from one to ten. **The final rating** is based on user reviews.

## **Technical overview**

For the full description pls follow by the link after the app is run - <a href="http://127.0.0.1:8000/redoc" target="_blank">Redoc</a>

## **User roles:**

* **Guest**: has rights to read comments and see ratings.

* **Authenticated user**: has rights to publish their own reviews, leave comments, rate works of art.

* **Moderator**: has rights to delete and correct any reviews and comments.

* **Administrator**: has rights to create and delete works of art, categories and genres, assign roles to users.

* **Superuser Django**: has full rights to manage the community.

## **Getting Started:**

Clone the repository:

>*git clone git@github.com:airatns/api_yamdb.git*

Set up the virtual environment:

>*python -m venv env* \
>*source env/scripts/activate*

Install dependencies in the app using requirements.txt:

>*python -m pip install --upgrade pip* \
>*pip install -r requirements.txt*

Run migrations:

>*python manage.py migrate*

Import test data:

>*python manage.py load_data*

Run the app locally:

>*python manage.py runserver*

## **New user registration**
To sign up enter the **email** and **username**.

Then a letter with **confirmation_code** will be sent to your email.

![code](https://user-images.githubusercontent.com/96816183/182865245-3efea538-0ec7-4d16-b8cc-a2a16c1edff4.png)

## **Getting a JWT-token**
To sign in enter **username** and **confirmation_code**.

A **token** will be issued for you.

The validity period of the token is **14 days**.

![token](https://user-images.githubusercontent.com/96816183/182865510-7f50333d-cf47-40d5-926d-5bcecbb2081d.png)

### **Example of using a JWT-token**

>*Bearer ey8Df...*


## **Examples of requests**

### **Changing your credentials**

![bio](https://user-images.githubusercontent.com/96816183/182865718-c9ba2d37-d00f-4a6f-8ecd-eb06a9376adc.png)

### **Deleting a genre**

![delete](https://user-images.githubusercontent.com/96816183/182865799-c96ff4d1-be79-4d89-ac7f-2f440c695f8b.png)

### **Adding a work of art**

![title](https://user-images.githubusercontent.com/96816183/182866123-b80f1a88-dbd5-497b-bb0d-4248252db3d9.png)
