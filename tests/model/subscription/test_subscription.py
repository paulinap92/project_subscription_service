from myproj.model.subscription import Subscription
from decimal import Decimal
import pytest

import pytest
from decimal import Decimal

def test_set_active():
    subscription = Subscription(
        user_id=1,
        service_id=2,
        quantity_per_month=3,
        discount=Decimal('5.00'),
        id_=10,
        active=False  # Początkowy stan jest ustawiony na False
    )

    subscription.set_active()  # Wywołujemy metodę, która ma ustawić active na True
    assert subscription.active is True  # Sprawdzamy, czy active jest True

def test_set_inactive():
    subscription = Subscription(
        user_id=1,
        service_id=2,
        quantity_per_month=3,
        discount=Decimal('5.00'),
        id_=10,
        active=True  # Początkowy stan jest ustawiony na True
    )

    subscription.set_inactive()  # Wywołujemy metodę, która ma ustawić active na False
    assert subscription.active is False  # Sprawdzamy, czy active jest False

def test_set_active_when_already_active():
    subscription = Subscription(
        user_id=1,
        service_id=2,
        quantity_per_month=3,
        discount=Decimal('5.00'),
        id_=10,
        active=True  # Początkowy stan jest ustawiony na True
    )

    subscription.set_active()  # Ponownie wywołujemy metodę set_active
    assert subscription.active is True  # Sprawdzamy, czy active nadal jest True

def test_set_inactive_when_already_inactive():
    subscription = Subscription(
        user_id=1,
        service_id=2,
        quantity_per_month=3,
        discount=Decimal('5.00'),
        id_=10,
        active=False  # Początkowy stan jest ustawiony na False
    )

    subscription.set_inactive()  # Ponownie wywołujemy metodę set_inactive
    assert subscription.active is False  # Sprawdzamy, czy active nadal jest False