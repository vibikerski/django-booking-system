## Django project for booking rooms

This is a basic project, which displays hotels and allows booking rooms from them. This project uses Django and Bootstrap. You can filter hotels and rooms depending on your needs. 

## Usage

Clone this repository:

```sh
$ git clone https://github.com/vibikerski/django-booking-system.git
$ cd django-booking-system
```

Create and activate a virtual Python enviroment. Then, install dependencies:

```sh
$ pip install -r requirements.txt
```

You can set up a superuser to add example entities:

```sh
$ python manage.py createsuperuser
```

To activate the server, run:
```sh
$ python manage.py runserver
```

and navigate to `http://127.0.0.1:8000/booking_system/` for the main page or `http://127.0.0.1:8000/booking_system/admin/` to add entities.