from myproj.model.user import User, Destination
from myproj.model.service import Service
from myproj.service.service import ServiceRepo
from myproj.model.subscription import Subscription
from myproj.file_repo.file_reader_factory import JsonData, TextData
from decimal import Decimal
from datetime import date
import unittest

import pytest


def test_subscriptions_for_user_id(user_service, expected_subscription):
    user_id = 1
    result = user_service.subscriptions_for_user_id(user_id)
    assert result == [expected_subscription]

def test_users_subscribed_to_service(user_service, expected_user_1):
    service_id = 1
    result = user_service.users_subscribed_to_service(service_id)
    assert result == [expected_user_1]


def test_subscribe_user_to_service(user_service):
    user_id = 1
    service_id = 1
    quantity_per_month = 5
    discount = Decimal('20.00')
    new_subscription = Subscription(1, 1, 5, Decimal('20.00'), 3)
    result = user_service.subscribe_user_to_service(user_id, service_id, quantity_per_month, discount)
    assert result == new_subscription



def test_active_subscriptions_report(user_service):

    result = user_service.active_subscriptions_report()
    expected_report = { User('Andrés', 'Logroño', Destination.CM, date(1992,12,2), 1):
            [Service(1, "Superfood", "Food", Decimal("10.00"))]}
    assert result == expected_report

