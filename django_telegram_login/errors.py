"""
Errors.
"""


class NotTelegramDataError(Exception):
    """
    Error for data that was hacked.
    """
    pass


class TelegramDataIsOutdatedError(Exception):
    """
    Error for outdated data.
    """
    pass
