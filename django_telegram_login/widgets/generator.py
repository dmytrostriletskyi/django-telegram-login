"""
Widgets generator interface.
"""
from django_telegram_login.widgets.constants import SMALL

WIDGET_SCRIPT_START = '<script async src="https://telegram.org/js/telegram-widget.js?3" '
WIDGET_SCRIPT_END = '></script>'
WIDGET_ONAUTH = 'data-onauth="onTelegramAuth(user)" '
ACCESS_WRITE_DEFAULT = True


def _generate_widget_parameters(bot_name, user_photo, size, corner_radius, access_write):
    """
    Generate common widget embed code parameters.
    """
    user_photo_bool = str(user_photo).lower()

    data_telegram_login = 'data-telegram-login="{}" '.format(bot_name)
    data_size = 'data-size="{}" '.format(size)
    data_userpic = 'data-userpic="{}" '.format(user_photo_bool) if not user_photo else ''
    data_radius = 'data-radius="{}" '.format(corner_radius) if corner_radius else ''
    data_request_access = 'data-request-access="write"' if access_write else ''

    return data_telegram_login, data_size, data_userpic, data_radius, data_request_access


def create_callback_login_widget(
        bot_name,
        size=SMALL,
        corner_radius=None,
        user_photo=True,
        access_write=ACCESS_WRITE_DEFAULT
):
    """
    Create a callback widget, that allows to handle an user data in JavaScript (onTelegramAuth func).
    """
    data_telegram_login, data_size, data_userpic, data_radius, data_request_access = \
        _generate_widget_parameters(bot_name, user_photo, size, corner_radius, access_write)

    return WIDGET_SCRIPT_START \
        + data_telegram_login \
        + data_size \
        + data_userpic \
        + data_radius \
        + WIDGET_ONAUTH \
        + data_request_access \
        + WIDGET_SCRIPT_END


def create_redirect_login_widget(
        redirect_url,
        bot_name,
        size=SMALL,
        corner_radius=None,
        user_photo=True,
        access_write=ACCESS_WRITE_DEFAULT
):
    """
    Create a redirect widget, that allows to handle an user data as get request parameters.
    """
    data_auth_url = 'data-auth-url="{}" '.format(redirect_url)

    data_telegram_login, data_size, data_userpic, data_radius, data_request_access = \
        _generate_widget_parameters(bot_name, user_photo, size, corner_radius, access_write)

    return WIDGET_SCRIPT_START \
        + data_telegram_login \
        + data_size \
        + data_userpic \
        + data_radius \
        + data_auth_url \
        + data_request_access \
        + WIDGET_SCRIPT_END
