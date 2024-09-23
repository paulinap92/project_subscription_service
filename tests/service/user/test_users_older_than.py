from myproj.model.user import User, Destination
from myproj.service.user import UserRepo
from datetime import date
import pytest
import unittest
from unittest.mock import MagicMock, Mock, patch
import logging

class TestUsersOlderThanWithMockedData(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.user_service = UserRepo([

            User('John', 'Smith', Destination.CM, date(1968, 11, 1), 1),
            User('Jan', 'Nowak', Destination.CM, date(2000, 12, 15), 2),
            User('Kevin', 'Doria', Destination.PN, date(2000, 10, 27), 3)
        ])

        cls.mock_today = patch('datetime.date').start()
        cls.mock_today.today.return_value = date(2000, 10, 26)

    def test_user_service_get_older_than(self):
        result = self.user_service.get_users_older_than(30)
        print(self.user_service)
        self.assertEqual(1, len(result))


    @classmethod
    def tearDownClass(cls) -> None:
        cls.mock_today.stop()
