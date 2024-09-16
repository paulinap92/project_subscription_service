from myproj.model.subscription import Subscription
from decimal import Decimal
import pytest

# user_id: int
# service_id: int
# quantity_per_month: int
# discount: Decimal | None = None
# id_: int | None = None
# active: bool | None = True

def test_when_user_id_will_be_updated():
    data = {'user_id': 100}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=100, service_id=1, quantity_per_month=1)
    assert expected_subscription == updated_subscription

def test_when_service_id_will_be_updated():
    data = {'service_id': 100}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=1, service_id=100, quantity_per_month=1)
    assert expected_subscription == updated_subscription

def test_when_service_and_user_id_will_be_updated():
    data = {'user_id': 101,'service_id': 102}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=101, service_id=102, quantity_per_month=1)
    assert expected_subscription == updated_subscription

def test_when_quantity_will_be_updated():
    data = {'quantity_per_month': 100}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=1, service_id=1, quantity_per_month=100)
    assert expected_subscription == updated_subscription

def test_when_discount_will_be_updated():
    data = {'discount': Decimal('100.11')}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal('10.02'))
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, discount=Decimal('100.11'))
    assert expected_subscription == updated_subscription

def test_when_id_will_be_updated():
    data = {'id_': 100}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, id_=10)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1,id_=100)
    assert expected_subscription == updated_subscription

def test_when_active_will_be_updated():
    data = {'active': False}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, id_=100, active=True)
    updated_subscription = subscription.update(data)
    expected_subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, id_=100, active=False)
    assert expected_subscription == updated_subscription


def test_when_no_updated():
    data = {}
    subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, id_=10, active=True)
    expected_subscription = Subscription(user_id=1, service_id=1, quantity_per_month=1, id_=10, active=True)
    updated_subscription = subscription.update(data)
    assert expected_subscription == updated_subscription
