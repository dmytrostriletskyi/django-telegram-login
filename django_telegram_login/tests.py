"""
Tests for django-telegram-login.
"""
import unittest

import mock

from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.widgets.constants import (
    SMALL,
    MEDIUM,
    LARGE,
    DISABLE_USER_PHOTO,
)
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)
from django_telegram_login.errors import (
    NotTelegramDataError,
    TelegramDataIsOutdatedError,
)


class TestAuthentication(unittest.TestCase):
    """
    Tests for athentication functionality.
    """

    def setUp(self):
        self.bot_token = '459236585:AAEee0Ba4fRijf1BRNbBO9W-Ar15F2xgV98'

        self.request_data = {
            'id': '299661134',
            'first_name': 'Dmytro',
            'last_name': 'Striletskyi',
            'username': 'dmytrostriletskyi',
            'photo_url': 'https://t.me/i/userpic/320/dmytrostriletskyi.jpg',
            'auth_date': '1518392724',
            'hash': '92ee8156a1482919843bfbaed2a91839f6594b2b98d884046c48ff58fa3a5ace'
        }

    @mock.patch('django_telegram_login.authentication.time.time')
    def test_ok_data(self, mock_time):
        """
        Received data is correct.
        """
        # auth_date and time now in unix datetime format are the same
        mock_time.return_value = 1518392724

        expected = self.request_data.copy()
        expected.pop('hash', None)

        result = verify_telegram_authentication(self.bot_token, self.request_data)
        self.assertEqual(expected, result)

    @mock.patch('django_telegram_login.authentication.time.time')
    def test_wrong_token(self, mock_time):
        """
        Wrong token.
        """
        # auth_date and time now in unix datetime format are the same
        mock_time.return_value = 1518392724

        request_data = self.request_data.copy()
        request_data['hash'] = '92ee8156a1482919843bfbaed2a91839f6594b2b98d884046c48ff58fa3a13c29'

        with self.assertRaises(NotTelegramDataError):
            verify_telegram_authentication(self.bot_token, request_data)

    def test_outdatet_data(self):
        """
        Outdated data.
        """
        request_data = self.request_data.copy()
        request_data['auth_date'] = '10'

        with self.assertRaises(TelegramDataIsOutdatedError):
            verify_telegram_authentication(self.bot_token, request_data)


class TestWidgetGenerator(unittest.TestCase):
    """
    Tests for creation widgets.
    """

    def setUp(self):

        self.bot_name = 'django_telegram_bot'
        self.redirect_url = 'https://django-telegram-login.com'

        widget_script_start = \
            """<script async src="https://telegram.org/js/telegram-widget.js?3" data-telegram-login="{}" """.format(
                self.bot_name
            )

        callback_widget_script_end = \
            """data-onauth="onTelegramAuth(user)" data-request-access="write"></script>"""

        redirect_widget_script_end = \
            """data-auth-url="{}" data-request-access="write"></script>""".format(self.redirect_url)

        self.expected_callback_small = \
            widget_script_start + """data-size="small" """ + callback_widget_script_end
        self.expected_callback_medium = \
            widget_script_start + """data-size="medium" """ + callback_widget_script_end
        self.expected_callback_large = \
            widget_script_start + """data-size="large" """ + callback_widget_script_end
        self.expected_callback_no_photo = \
            widget_script_start + """data-size="small" data-userpic="false" """ + callback_widget_script_end
        self.expected_callback_corner_radius = \
            widget_script_start + \
            """data-size="small" data-userpic="false" data-radius="1" """ + \
            callback_widget_script_end

        self.expected_redirect_small = \
            widget_script_start + """data-size="small" """ + redirect_widget_script_end
        self.expected_redirect_medium = \
            widget_script_start + """data-size="medium" """ + redirect_widget_script_end
        self.expected_redirect_large = \
            widget_script_start + """data-size="large" """ + redirect_widget_script_end
        self.expected_redirect_no_photo = \
            widget_script_start + """data-size="small" data-userpic="false" """ + redirect_widget_script_end
        self.expected_redirect_corner_radius = \
            widget_script_start + \
            """data-size="small" data-userpic="false" data-radius="10" """ + \
            redirect_widget_script_end

    def test_callback_small(self):
        """
        Test creation of small callback login widget.
        """
        result = create_callback_login_widget(self.bot_name, size=SMALL)
        self.assertEqual(self.expected_callback_small, result)

    def test_callback_medium(self):
        """
        Test creation of medium callback login widget.
        """
        result = create_callback_login_widget(self.bot_name, size=MEDIUM)
        self.assertEqual(self.expected_callback_medium, result)

    def test_callback_large(self):
        """
        Test creation of large callback login widget.
        """
        result = create_callback_login_widget(self.bot_name, size=LARGE)
        self.assertEqual(self.expected_callback_large, result)

    def test_callback_corner_radius(self):
        """
        Test creation of callback login widget with specified corner radius.
        """
        result = create_callback_login_widget(self.bot_name, corner_radius=1, user_photo=DISABLE_USER_PHOTO)
        self.assertEqual(self.expected_callback_corner_radius, result)

    def test_callback_no_photo(self):
        """
        Test creation of callback login widget without photo.
        """
        result = create_callback_login_widget(self.bot_name, user_photo=DISABLE_USER_PHOTO)
        self.assertEqual(self.expected_callback_no_photo, result)

    def test_redirect_small(self):
        """
        Test creation of small redirect login widget.
        """
        result = create_redirect_login_widget(self.redirect_url, self.bot_name, size=SMALL)
        self.assertEqual(self.expected_redirect_small, result)

    def test_redirect_medium(self):
        """
        Test creation of medium redirect login widget.
        """
        result = create_redirect_login_widget(self.redirect_url, self.bot_name, size=MEDIUM)
        self.assertEqual(self.expected_redirect_medium, result)

    def test_redirect_large(self):
        """
        Test creation of large redirect login widget.
        """
        result = create_redirect_login_widget(self.redirect_url, self.bot_name, size=LARGE)
        self.assertEqual(self.expected_redirect_large, result)

    def test_redirect_corner_radius(self):
        """
        Test creation of redirect login widget with specified corner radius.
        """
        result = create_redirect_login_widget(
            self.redirect_url, self.bot_name, corner_radius=10, user_photo=DISABLE_USER_PHOTO
        )
        self.assertEqual(self.expected_redirect_corner_radius, result)

    def test_redirect_no_photo(self):
        """
        Test creation of redirect login widget without photo.
        """
        result = create_redirect_login_widget(
            self.redirect_url, self.bot_name, user_photo=DISABLE_USER_PHOTO
        )
        self.assertEqual(self.expected_redirect_no_photo, result)


if __name__ == '__main__':
    unittest.main()
