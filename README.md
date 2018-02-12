# Django-telegram-login

Django application for Telegram login intefrace and widget handling.

[![Release](https://img.shields.io/github/release/dmytrostriletskyi/django-telegram-login.svg)](https://github.com/dmytrostriletskyi/django-telegram-login/releases)
![Build](https://api.travis-ci.org/dmytrostriletskyi/django-telegram-login.svg?branch=develop)
![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

[![Medium](https://img.shields.io/badge/Post-Medium-brightgreen.svg)](url)
[![Habrahabr](https://img.shields.io/badge/Post-Habrahabr-brightgreen.svg)](url)

## Getting started

### How to install

```
$ pip3 install django-telegram-login
```

## Development

Install packages that needed for the testing:

```
$ pip3 install requirements-dev.txt
```

Run the tests before development to be sure that `django-telegram-login` works properly:

```
$ python -m unittest discover
```

Follow a codestyle with linters:

```
$ flake8 django_telegram_login && pycodestyle django_telegram_login && pylint django_telegram_login
```
