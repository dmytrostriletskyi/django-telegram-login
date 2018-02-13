"""
Widgets generator interface.
"""
from django_telegram_login.widgets.constants import SMALL


def create_callback_login_widget(
        bot_name, size=SMALL, corner_radius=None, user_photo=True, access_write=True
):
    """
    Create callback widget, that allows to handle user data in JavaSccript.
    """
    script_initital = '<script async src="https://telegram.org/js/telegram-widget.js?3" '
    bot = 'data-telegram-login="{}" '.format(bot_name)
    size = 'data-size="{}" '.format(size)
    userpic = 'data-userpic="{}" '.format(str(user_photo).lower()) if not user_photo else ''
    corner_radius = 'data-radius="{}" '.format(corner_radius) if corner_radius else ''
    onauth = 'data-onauth="onTelegramAuth(user)" '
    access = 'data-request-access="write"' if access_write else ''
    script_end = '></script>'

    widget_script = script_initital + bot + size + userpic + corner_radius + onauth + access + script_end
    return widget_script


def create_redirect_login_widget(
        redirect_url, bot_name, size=SMALL, corner_radius=None, user_photo=True, access_write=True
):
    """
    Create redirect widget, that allows to handle user data as get request params.
    """
    script_initital = '<script async src="https://telegram.org/js/telegram-widget.js?3" '
    bot = 'data-telegram-login="{}" '.format(bot_name)
    size = 'data-size="{}" '.format(size)
    userpic = 'data-userpic="{}" '.format(str(user_photo).lower()) if not user_photo else ''
    corner_radius = 'data-radius="{}" '.format(corner_radius) if corner_radius else ''
    redirect = 'data-auth-url="{}" '.format(redirect_url)
    access = 'data-request-access="write"' if access_write else ''
    script_end = '></script>'

    widget_script = script_initital + bot + size + userpic + corner_radius + redirect + access + script_end
    return widget_script
