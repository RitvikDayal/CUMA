# Custom User Model and Authentication
----------------------------------------------------------------
## _Email based User registrations and 2-Factor Authentication_

This is a Django project that showcase custom user models, user management, and 2-factor authentication for login as well as registration.

> Stack: Django, PSQL 

## Features

- Custom Login, Logout templates
- Password reset functionality
- 2-Factor Authentication using Email (SMTP)
- Custom User model (E-mail based)
- User Profile system
- Custom Logs

## Installation

CUMA requires [Python](https://www.python.org/downloads/release/python-379/) v3.7.9+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd CUMA
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
> **Note**: Setup the environ variables before running the server.
- SECRET_KEY
- DEBUG

After setting up the environ variables.
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

