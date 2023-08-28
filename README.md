# Catalog

This repository represents my implementation for the [Backend Technical Test](https://github.com/luuna-tech/test/blob/master/backend/README.md) applied by Zebrands.

## Installation

Clone this repository

    git clone https://github.com/2Fac3R/catalog.git

Create or start your virtual environment [venv](https://docs.python.org/3/library/venv.html)

    python3 -m venv .venv
    source .venv/bin/activate

Install requirements. Use the package manager [pip](https://pip.pypa.io/en/stable/)

    pip3 install -r requirements.txt

Make migrations and migrate

    python3 manage.py makemigrations
    python3 manage.py migrate

Create a superuser

    python3 manage.py createsuperuser

Run the server

    python3 manage.py runserver

You can now access the server at http://localhost:8000

## Usage

Log in

    http://localhost:8000/admin

You can access to the following routes

    http://localhost:8000/api/v1/users/
    http://localhost:8000/api/v1/groups/
    http://localhost:8000/api/v1/products/
    http://localhost:8000/catalog/products/
    http://localhost:8000/catalog/products/1


API Documentation routes

    http://localhost:8000/swagger
    http://localhost:8000/redoc


You can also use the Django Rest Framework Browsable API for testing the application.

## Description

I decided to use the following packages:

* [djangorestframework](https://www.django-rest-framework.org/) It's a powerful and flexible toolkit for building Web APIs.
* [django-notifications-hq](https://pypi.org/project/django-notifications-hq/) Notification system.
* [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code.
* [django-filter](https://django-filter.readthedocs.io/en/stable/) Reusable Django app allowing users to add dynamic QuerySet filtering from URL parameters.

You can find more details in *requirements.txt* file.

## TODO:
* User activity tracking feature.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Any feedback is appreciated.