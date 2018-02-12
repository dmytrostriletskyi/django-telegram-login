import base64
import hashlib
import hmac
import time

from django_telegram_login.errors import (
    NotTelegramDataError, 
    TelegramDataIsOutdatedError,
)

ONE_DAY_IN_SECONDS = 86400


def verify_telegram_authentication(bot_token, request_data):
    request_data = request_data.copy()

    recieved_hash = request_data['hash']
    auth_date = request_data['auth_date']

    request_data.pop('hash', None)
    request_data_alphabetical_order = sorted(request_data.items(), key=lambda x: x[0])

    data_check_string = []

    for data_pair in request_data_alphabetical_order:
        key, value = data_pair[0], data_pair[1]
        data_check_string.append(key + '=' + value)

    data_check_string = '\n'.join(data_check_string)

    secret_key = hashlib.sha256(bot_token.encode()).digest()
    _hash = hmac.new(secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()

    unix_time_not = int(time.time())
    unix_time_auth_date = int(auth_date)

    if _hash != recieved_hash:
        raise NotTelegramDataError(
                'This is not a Telegram data. Hash from recieved authentication data does not match'
                'with calculated hash based on bot token.'
            )

    if unix_time_not - unix_time_auth_date > ONE_DAY_IN_SECONDS:
        raise TelegramDataIsOutdatedError(
                'Authentication data is outdated. Authentication was received more than day ago.'
            )

    return request_data