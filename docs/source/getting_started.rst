Getting started
===============

Preparation
^^^^^^^^^^^

Telegram login inteface (API) requires a website with domain. However you may want to ask how to develop telegram login on a localhost?

Install ``localtunnel`` tool with the following command (be sure that you have a ``npm``)::

    $ npm install -g localtunnel

Run a tunnel on the port that you are going to specify for the Django runserver's command. In our case it is a 8000::

    $ lt --port 8000

You will receive a url, for example ``https://gqgh.localtunnel.me``, that you can share with anyone for as long as your local instance of localtunnel remains active. Any requests will be routed to your local service at the specified port.

Use received url anywhere in the development — specify in settings, set as domain (``/setdomain`` command) for ``@BotFather`` and browse it - ``https://gqgh.localtunnel.me/redirect/`` instead of ``127.0.0.1:8000/redirect/``.

Installation
^^^^^^^^^^^^

Instal package via ``pip``::

    $ pip install django-telegram-login

Settings
^^^^^^^^

Add application to the installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_telegram_login',
    ]

If you use only one bot you are able to add the following settings to own ``settings.py`` in Django project::

    TELEGRAM_BOT_NAME = 'django_telegram_login_bot'
    TELEGRAM_BOT_TOKEN = '459236585:AAEee0Ba4fRijf1BRNbBO9W-Ar15F2xgV98'
    TELEGRAM_LOGIN_REDIRECT_URL = 'https://gqgh.localtunnel.me'

And use them in cases below::

    from django.conf import settings


    bot_name = settings.TELEGRAM_BOT_NAME
    bot_token = settings.TELEGRAM_BOT_TOKEN
    redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

But ``django-telegram-login`` allows you to use unlimited bots as you will see during learing the package.
