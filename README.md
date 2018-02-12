# Django-telegram-login

Django application for Telegram login intefrace and widget handling.

[![Release](https://img.shields.io/github/release/dmytrostriletskyi/django-telegram-login.svg)](https://github.com/dmytrostriletskyi/django-telegram-login/releases)
![Build](https://api.travis-ci.org/dmytrostriletskyi/django-telegram-login.svg?branch=develop)
![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

[![Medium](https://img.shields.io/badge/Post-Medium-brightgreen.svg)](url)
[![Habrahabr](https://img.shields.io/badge/Post-Habrahabr-brightgreen.svg)](url)

## Getting started

First of all, please, if you want to implement Telegram login into website, check the official [news](https://telegram.org/blog/login) and the [widgets documentation](https://core.telegram.org/widgets/login).

### Preparation

Telegram login inteface (API) requires a website with domain. But you may want to ask, how to develop telegram login on localhost?

Install `localtunnel` tool with following command (be sure you have npm installed).

```bash
$ npm install -g localtunnel
```

Run a tunnel on the port that you are going to specifed for the Django runserver's command. In out example it is a 8000.

```bash
$ lt --port 8000
```

You will receive a url, for example `https://gqgh.localtunnel.me`, that you can share with anyone for as long as your local instance of lt remains active. Any requests will be routed to your local service at the specified port.

Use received url anywhere in development - specify in the settings, set as domain for @[BotFather](t.me/BotFather).
In production use true domain.

### Install

```bach
$ pip3 install django-telegram-login
```

### Additional settings

Add application to installed apps.

```python
INSTALLED_APPS = [
    ...
    'telegram_django_telegram_loginauth'
]
```

If you use only one bot you are able to add following settings to own `settings.py` in Django project:

```python
TELEGRAM_BOT_NAME = 'django_telegram_login_bot'
TELEGRAM_BOT_TOKEN = '459236585:AAEee0Ba4fRijf1BRNbBO9W-Ar15F2xgV98'
TELEGRAM_LOGIN_REDIRECT_URL = 'https://iyjjvnvszx.localtunnel.me/'
```

And use them in cases below:

```python
from django.conf import settings


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL
```

But `django-telegram-login` allow you to use unlimited bots (will see in examples below).

## How to use

### Types of login and widgets

You are able to make two reaction on user tap on button: callback and redirect.
`Callback` allows you to handle user data currently on page with button - you will receive data from Telegram in special JavaScript-function handler.

```javascript
<script type="text/javascript">
  function onTelegramAuth(user) {
    alert('Logged in as ' + user.first_name + ' ' + user.last_name + '!');
  }
</script>
```

So you can handle in on front-end or make `AJAX` call to back-end and transfer data.

`Redirect` redirects user to specified link - link will contain user data in get request params in url.

```bash
[12/Feb/2018 03:32:04] "GET /?id=299661134&first_name=Dmytro&last_name=Striletskyi&username=dmytrostriletskyi&photo_url=https%3A%2F%2Ft.me%2Fi%2Fuserpic%2F320%2Fdmytrostriletskyi.jpg&auth_date=1518406180&hash=f5cd61a87131fcf51fc745d465a36bdcc58db4175ccac7c5afbf641359f55807 HTTP/1.1" 200 14
```

So get it in `request.GET` into your view that handle specified url.

There are for now 6 type if widget interfaces you can customize with `django-telegram-api`: small, medium and large; with and withut photo.

![](https://habrastorage.org/webt/lh/xz/hw/lhxzhwrligxu4rsm-voqb2xovee.png)

![](https://habrastorage.org/webt/_d/g_/eu/_dg_eu-vtcl3ezdko0qyih_lf7k.png)

![](https://habrastorage.org/webt/3x/ed/ku/3xedkuddyzwt5d9zdvbupelrhn4.png)

![](https://habrastorage.org/webt/un/bv/ec/unbveca7gdzzeiwv2jhhwajdnvm.png)

![](https://habrastorage.org/webt/s7/ps/h5/s7psh5amj5a7fnndlw9bkl7otx8.png)

![](https://habrastorage.org/webt/y0/ef/u3/y0efu36pcmghb60kukbf8sw2yjk.png)

It is too easy and native. Import size constants and constant for disabling photo.

```python
from django_telegram_login.widgets.constants import (
    SMALL, 
    MEDIUM, 
    LARGE,
    DISABLE_USER_PHOTO,
)
```

Import widget generator function.

```python
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)
```

Generate with according functions your widget.

```python
telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)

telegram_login_widget = create_redirect_login_widget(
  redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
)
```

Widget generator returns string that contains JavaScript code. This code automaticaly create widget (button)
and handle user taps (request) on its own.

So use it in your views via context.

```python
def callback(request):
    telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'telegram_auth/callback.html', context)


def redirect(request):
    telegram_login_widget = create_redirect_login_widget(
        redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
    )

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'telegram_auth/redirect.html', context)
```

Do not forget make safe render of it, because it is not raw text, but Javascript. Jinja code is the followinf code.

```html
{% autoescape off %}{{ telegram_login_widget }}{% endautoescape %}
```

Full bunch of examples are open [here](https://github.com/dmytrostriletskyi/django-telegram-login/tree/develop/examples).

### Telegram authentication

There are may be the situations, when bad boys will send you incorrect Telegram data (pretend that it is from user).
`django-telegram-login` provide following way to ensure, that data is correct and isn't hacked.

```python
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import (
    NotTelegramDataError, 
    TelegramDataIsOutdatedError,
)


def index(request):
    try:
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

    except TelegramDataIsOutdatedError:
        return HttpResponse('Authentication was received more than day ago.')

    except NotTelegramDataError:
        return HttpResponse('Data is not relates to Telegram!')

    # Or handle it like you want. For example, save to DB. :)
    return HttpResponse('Hello, ' + result['first_name'] + '!')
```

`verify_telegram_authentication` implements a Telegram [instructions](https://core.telegram.org/widgets/login#checking-authorizations) to verify the authentication. If result does not raise errors, It will be return dictionary of user data.

`TelegramDataIsOutdatedError` - user data alive for one day only.
`NotTelegramDataError` - incorrect data.

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
