from myproj.model.service import Service
from decimal import Decimal
import pytest

def test_when_name_will_be_updated():
    data = {'name': 'X'}
    service = Service(id_=1, name='A', category='Food', price=Decimal(100))
    updated_service = service.update(data)
    expected_service = Service(id_=1, name='X',category='Food', price=Decimal(100))
    assert expected_service == updated_service

def test_when_price_will_be_updated():
    data = {'price': Decimal(1000)}
    service = Service(id_=1, name='A', category='Food', price=Decimal(100))
    updated_service = service.update(data)
    expected_service = Service(id_=1, name='A', category='Food', price=Decimal(1000))
    assert expected_service == updated_service

def test_when_name_and_price_will_be_updated():
    data = {'name': 'X', 'price': Decimal(1000)}
    service = Service(id_=1, name='A', category='Food', price=Decimal(100))
    updated_service = service.update(data)
    expected_service = Service(id_=1, name='X', category='Food', price=Decimal(1000))
    assert expected_service == updated_service

def test_when_no_updated():
    data = {}
    service = Service(id_=1, name='A', category='Food', price=Decimal(100))
    expected_service = Service(id_=1, name='A', category='Food', price=Decimal(100))
    updated_service = service.update(data)
    assert expected_service == updated_service