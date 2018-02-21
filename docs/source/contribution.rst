Contribution
============

Issues
^^^^^^

If you find an issue or a bug, or you want to request any feautre, feel free to use `Github issues <https://github.com/dmytrostriletskyi/django-telegram-login/issues>`_.

Pull requests
^^^^^^^^^^^^^

If you want to impove ``django-telegram-login`` or resolve any issue, please use `Github pull requests <https://github.com/dmytrostriletskyi/django-telegram-login/pulls>`_.

Development
^^^^^^^^^^^

Follow `this code style <http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/style_guides/python-guidelines.html>`_ in your development, please.

Install the packages required for development::

    $ pip install -r requirements-dev.txt

Run the tests before development to make sure ``django-telegram-login`` logic works properly::

    $ python -m unittest discover

Follow a codestyle with the following linters::

    $ flake8 django_telegram_login && pycodestyle django_telegram_login && pylint django_telegram_login
