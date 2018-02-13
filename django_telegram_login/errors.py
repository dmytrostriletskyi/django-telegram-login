"""
Errors.
"""


class NotTelegramDataError(Exception):
    """
    The verification algorithm did not authorize a Telegram data.
    """
    pass


class TelegramDataIsOutdatedError(Exception):
    """
    The Telegram data is outdated
    """
    pass
