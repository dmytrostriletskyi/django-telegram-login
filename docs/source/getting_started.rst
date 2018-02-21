Getting started
===============

Telegram login inteface (API) requires a website with domain. However you may want to ask how to develop telegram login on a localhost?

Install ``localtunnel`` tool with the following command (be sure that you have a ``npm``)::

    $ npm install -g localtunnel

Run a tunnel on the port that you are going to specify for the Django runserver's command. In our case it is a 8000::

    $ lt --port 8000

You will receive a url, for example ``https://gqgh.localtunnel.me``, that you can share with anyone for as long as your local instance of localtunnel remains active. Any requests will be routed to your local service at the specified port.

Use received url anywhere in the development - specify in settings, set as domain (``/setdomain`` command) for ``@BotFather`` and browse it - ``https://gqgh.localtunnel.me/redirect/`` instead of ``127.0.0.1:8000/redirect/``.

Preparation
^^^^^^^^^^^

Preparation


Installation
^^^^^^^^^^^^

Installation


Settings
^^^^^^^^

Settings