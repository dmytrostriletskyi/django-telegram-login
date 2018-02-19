"""
Telegram login errors.
"""


class NotTelegramDataError(Exception):
    """
    The verification algorithm did not authorize Telegram data.
    """
    pass


class TelegramDataIsOutdatedError(Exception):
    """
    The Telegram data is outdated.
    """
    pass
