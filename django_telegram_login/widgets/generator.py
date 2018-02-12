"""
Widgets generator interface.
"""
from django_telegram_login.widgets.constants import (
    SMALL, 
    MEDIUM, 
    LARGE,
    DISABLE_USER_PHOTO
)

def create_callback_login_widget(bot_name, size=SMALL, user_photo=True, access_write=True):
    """
    Create callback widget, that allows to handle user data in JavaSccript.
    """
    script_initital = '<script async src="https://telegram.org/js/telegram-widget.js?2" '
    bot = 'data-telegram-login="{}" '.format(bot_name)
    size = 'data-size="{}" '.format(size)
    userpic = 'data-userpic="{}" '.format(user_photo) if not user_photo else ''
    onauth= 'data-onauth="onTelegramAuth(user)" '
    access = 'data-request-access="write"' if access_write else ''
    script_end = '></script>'

    widget_script = script_initital + bot + size + userpic + onauth + access + script_end
    return widget_script 


def create_redirect_login_widget(redirect_url, bot_name, size=SMALL, user_photo=True, access_write=True):
    """
    Create redirect widget, that allows to handle user data as get request params.
    """
    script_initital = '<script async src="https://telegram.org/js/telegram-widget.js?2" '
    bot = 'data-telegram-login="{}" '.format(bot_name)
    size = 'data-size="{}" '.format(size)
    userpic = 'data-userpic="{}" '.format(user_photo) if not user_photo else ''
    redirect = 'data-auth-url="{}" '.format(redirect_url)
    access = 'data-request-access="write"' if access_write else ''
    script_end = '></script>'

    widget_script = script_initital + bot + size + userpic + redirect + access + script_end
    return widget_script
