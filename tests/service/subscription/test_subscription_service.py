from myproj.service.subscription import SubscriptionRepo
from myproj.service.subscription import Subscription
from myproj.file_repo.file_reader_factory import JsonData, TextData
from decimal import Decimal
import unittest
from unittest.mock import MagicMock

import pytest


class TestDataToSubscription(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_json_subscription_data = MagicMock(spec=JsonData)
        cls.mock_text_subscription_data = MagicMock(spec=TextData)
        cls.mock_list_subscription_data = MagicMock(spec=list[Subscription])

    def setUp(self):
        self.expected_subscriptions = {
            1: Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal("10.00"), id_=1, active=True),
            2: Subscription(user_id=2, service_id=1, quantity_per_month=2, discount=Decimal("20.00"), id_=2, active=False)
            }
        self.subscriptions_repo = SubscriptionRepo([
            Subscription(1, 1, 1, Decimal("10.00"), 1, True),
            Subscription(2, 2, 2, Decimal("20.00"), 2, False),
            Subscription(3, 2, 1, Decimal("30.00"), 3, True)
        ])

    def test_data_convert_to_subscription_from_json(self):
        self.mock_json_subscription_data.get_content.return_value = {
            1: ['1', '1', '1', "10.00", '1', '1'],
            2: ['2', '1', '2', "20.00", '2', '0']
        }
        self.subscriptions_repo = SubscriptionRepo(self.mock_json_subscription_data)
        subscriptions = self.subscriptions_repo.get_subscriptions()

        self.assertEqual(subscriptions, self.expected_subscriptions)

    def test_data_convert_to_subscription_from_text(self):
        self.mock_text_subscription_data.get_content.return_value = [
            ['1', '1', '1', "10.00", '1', '1'],
            ['2', '1', '2', "20.00", '2', '0']
        ]

        subscriptions_repo = SubscriptionRepo(self.mock_text_subscription_data)
        subscriptions = subscriptions_repo.get_subscriptions()

        self.assertEqual(len(subscriptions), 2)
        self.assertEqual(subscriptions, self.expected_subscriptions)

    def test_data_convert_to_subscription_from_list(self):
        self.mock_list_subscription_data = [
            Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal("10.00"), id_=1, active=True),
            Subscription(user_id=2, service_id=1, quantity_per_month=2, discount=Decimal("20.00"), id_=2, active=False)
        ]
        subscriptions_repo = SubscriptionRepo(self.mock_list_subscription_data)
        subscriptions = subscriptions_repo.get_subscriptions()

        self.assertEqual(len(subscriptions), 2)
        self.assertEqual(subscriptions, self.expected_subscriptions)

    def test_not_correct_data_convert_to_subscription(self):
        with self.assertRaises(ValueError) as e:
            subscription_repo = SubscriptionRepo('fake_data')

    def test_add_subscription(self):
        new_subscription = Subscription(0, 1, 1, Decimal("15.00"), 4, True)
        added_subscription = self.subscriptions_repo.add_subscription(new_subscription)

        self.assertEqual(len(self.subscriptions_repo.get_subscriptions()), 4)
        self.assertEqual(added_subscription, new_subscription)

    def test_add_subscription_dict(self):
        new_subscription = {'user_id': 2, 'service_id' : 1, 'quantity_per_month': 2, 'discount': Decimal("20.00"),
                            'id_': 2, 'active': False}
        added_subscription = self.subscriptions_repo.add_subscription(new_subscription)
        transformed_subscription = Subscription(user_id=2, service_id=1, quantity_per_month=2, discount=Decimal("20.00"), id_=4, active=False)

        self.assertEqual(added_subscription, transformed_subscription)

    def test_find_by_id(self):
        found_subscription = self.subscriptions_repo.find_by_id(1)
        sub1 = Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal("10.00"), id_=1, active=True)
        self.assertEqual(found_subscription, sub1)

    def test_find_by_id_not_found(self):
        with self.assertRaises(KeyError):
            self.subscriptions_repo.find_by_id(50)

    def test_get_subscriptions_by_user_id(self):
        user_subscriptions = self.subscriptions_repo.get_subscriptions_by_user_id(1)
        sub1 = Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal("10.00"), id_=1,
                            active=True)
        self.assertEqual(len(user_subscriptions), 1)
        self.assertEqual(user_subscriptions, [sub1])

    def test_get_subscriptions_by_service_id(self):
        service_subscriptions = self.subscriptions_repo.get_subscriptions_by_service_id(2)
        sub1 = Subscription(user_id=2, service_id=2, quantity_per_month=2, discount=Decimal("20.00"), id_=2, active=False)
        sub2 = Subscription(3, 2, 1, Decimal("30.00"), 3, True)
        self.assertEqual(len(service_subscriptions), 2)
        self.assertEqual(service_subscriptions, [sub1, sub2])

    def test_get_all_subscriptions(self):
        all_subscriptions = self.subscriptions_repo.get_all_subscriptions()
        self.assertEqual(len(all_subscriptions), 3)

    def test_get_all_active_subscriptions(self):
        active_subscriptions = self.subscriptions_repo.get_all_active_subscriptions()
        self.assertEqual(len(active_subscriptions), 2)

    def test_update_subscription(self):
        update_data = {
            "discount": Decimal("99.00"),
        }
        self.subscriptions_repo.update(1, update_data)
        updated_subscription = self.subscriptions_repo.find_by_id(1)
        self.assertEqual(updated_subscription.discount, Decimal("99.00"))

    def test_delete_subscription(self):
        self.subscriptions_repo.delete(1)

        self.assertEqual(len(self.subscriptions_repo.get_subscriptions()), 2)

    def test_delete_subscription_not_found(self):
        with self.assertRaises(KeyError):
            self.subscriptions_repo.delete(2222)



