# Overview

Basic Implementation of Basic and Token Based Authentication of DjangoRestFramework

# Technnology Stack
Python3, Django, DjangoRestFramework, djangorestframework-simplejwt


# Installation
- Install Python3
- `cd $ProjectRoot`
- `cd pip3 install -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

# Creating a Superuser
- `python3 manage.py createsuperuser`

# URLs
## Auth Urls

- Getting AuthToken: `api/token/`
- Refreshing AuthToken `api/token/refresh/`
- Verifying AuthToken `api/token/verify/`

## View Urls
- `api/get_user/`: both for login user and anonymous user
- `api/get_auth_user/`: for login user only with both basic auth and token authentication
- `api/get_token_auth_user/`: for login user only with only token authentication
