How to use widgets
==================

Interface
^^^^^^^^^^^^^^^^^

.. image:: _static/logo.png

For now you are able to customize widget by the following arguments:

1. Size: small, medium, large.
2. User photo: show it near the button or not.
3. Corner radius: radius of corners from material to bootstrap style.

Login widgets types
^^^^^^^^^^^^^^^^^^^

You are able to make two reactions for user interaction with a button: ``callback`` and ``redirect``. 
Telegram response with the following data relates to login widgtes types: 

1. first_name: first name.
2. last_name: last name.
3. username: username.
4. photo_url: link to user's photo that located in Telegram storage
5. auth_date: Unix datetime (time in second from time when Unix was born)
6. hash: secret thing to verify data above.

**Callback** allows you to handle user data currently on page - you will receive data from Telegram in special ``JavaScript-function-handler`` (you need to implement it but save the name).

.. code-block:: javascript

    <script type="text/javascript">
        function onTelegramAuth(user) {
            alert('Logged in as ' + user.first_name + ' ' + user.last_name + '!');
        }
    </script>

So you can handle it on the front-end or make a ``AJAX`` call to back-end and transfer a data.

**Redirect** transfers user to the specified link.

.. code-block:: python

    telegram_login_widget = create_redirect_login_widget(
        redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
    )

It will contain an user's data in get request parameters.

.. code-block:: python

    [12/Feb/2018 03:32:04] "GET /
        ?id=299661134
        &first_name=Dmytro
        &last_name=Striletskyi
        &username=dmytrostriletskyi
        &photo_url=https%3A%2F%2Ft.me%2Fi%2Fuserpic%2F320%2Fdmytrostriletskyi.jpg
        &auth_date=1518406180
        &hash=f5cd61a87131fcf51fc745d465a36bdcc58db4175ccac7c5afbf641359f55807 
        HTTP/1.1" 200 14

So get it in ``request.GET`` within your view that handle request on specified URL.

Customizing
^^^^^^^^^^^

Customize **widgets interface** with the following parameters:

1. ``Size``: constants ``SMALL``, ``MEDIUM``, ``LARGE``.
2. ``User photo``: do not pass any parameters to enable by defaul or disable with ``DISABLE_USER_PHOTO`` constant.
3. ``Corner radius``: integer in range from 1 (material) to 20 (bootstrap, by default).

Customize **widgets login type** with the following parameters:

1. ``Bot name``: name of bot as string. 
2. ``Redirect URL`` (required only for the redirect widget): website address that will receive user's data by get request.

Import size constants, corner radius and a constant for disabling photo.

.. code-block:: python

    from django_telegram_login.widgets.constants import (
        SMALL, 
        MEDIUM, 
        LARGE,
        DISABLE_USER_PHOTO,
    )

Import widget generators functions.

.. code-block:: python

    from django_telegram_login.widgets.generator import (
        create_callback_login_widget,
        create_redirect_login_widget,
    )

Generate widgets according to provided functions.

.. code-block:: python

    telegram_callback_login_widget = create_callback_login_widget(bot_name, corner_radius=10, size=SMALL)

    telegram_callback_llogin_widget = create_redirect_login_widget(
        redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
    )

Rendering
^^^^^^^^^

Widget generator returns a string that contains ``JavaScript`` code. This code creates widget (button) automatically and handles user taps (requests) on its own. Your deal is to receive and process user data.

So use it in your views via context.

.. code-block:: python

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

Do not forget to make its rendering safe, because it is not a raw text but ``Javascript``. Below is an example of a ``Jinja code``.

.. code-block:: html

    {% autoescape off %} {{ telegram_login_widget }} {% endautoescape %}

Telegram authentication
^^^^^^^^^^^^^^^^^^^^^^^

There may be the situations, when hackers will send you incorrect Telegram data (pretending to be from a real user). ``django-telegram-login`` provides the following way to ensure that data is correct and isn't hacked.

.. code-block:: python

    from django_telegram_login.authentication import verify_telegram_authentication
    from django_telegram_login.errors import (
        NotTelegramDataError, 
        TelegramDataIsOutdatedError,
    )


    def index(request):

        # Initially, the index page may have no get params in URL
        # For example, if it is a home page, a user should be redirected from the widget
        if not request.GET.get('hash'):
            return HttpResponse('Handle the missing Telegram data in the response.')

        try:
            result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

        except TelegramDataIsOutdatedError:
            return HttpResponse('Authentication was received more than a day ago.')

        except NotTelegramDataError:
            return HttpResponse('The data is not related to Telegram!')

        # Or handle it as you wish. For instance, save to DB.
        return HttpResponse('Hello, ' + result['first_name'] + '!')

``verify_telegram_authentication`` implements Telegram `instructions <https://core.telegram.org/widgets/login#checking-authorization>`_ to verify the authentication. If result does not raise errors, it will return a dictionary with user data.

Errors:

1. ``NotTelegramDataError`` - the verification algorithm did not authorize Telegram data.
2. ``TelegramDataIsOutdatedError`` - The Telegram data is outdated.
