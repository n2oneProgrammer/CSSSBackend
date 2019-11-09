# Short installation guide

## First, install Python:
- Python 3.6, 3.7
- Django 2.2

We **highly recommend** and only officially support the latest patch release of each Python and Django series.

## Activate environment
Activate a virtual environment.
```
env\Scripts\activate
```

## Generate key
Generate a new private key, and put it in ./mysite/key.txt
```
django-admin shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'[GENERATED KEY]'
>>>
```

## Set up database
Set up date to contect to the database (We will use mysql database.) in ./mysite/mysite/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csss', #DB name
        'USER': 'root', #DB user name
        'PASSWORD': '',  #DB password
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306', # DB port (default is 3306)
    }
}
```

## Migration and sync the database
Create an initial migration for models, and sync the database for the first time.
```
python manage.py makemigrations mysite
python manage.py migrate
```


## Start up a server.
Before starting up python server start up DB server (for exampele XAMPP).
And after that start python server:
```
python manage.py runserver
```
