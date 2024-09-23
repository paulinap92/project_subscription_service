import pytest
from decimal import Decimal
from myproj.model.service import Service
from myproj.file_repo.file_reader_factory import JsonData, TextData
from myproj.service.service import ServiceRepo

@pytest.fixture
def expected_service_1():
    return Service(1, 'Superfood', 'Food', Decimal('10.00'))

@pytest.fixture
def expected_service_2():
    return Service(2, 'Superwine', 'Wine', Decimal('20.00'))

@pytest.fixture
def expected_service_repo(expected_service_1, expected_service_2):
    return ServiceRepo([expected_service_1, expected_service_2])

@pytest.fixture
def json_data():
    return JsonData({
            1: [1, 'Superfood', 'Food', '10.00'],
            2: [2, 'Superwine', 'Wine', '20.00']
        })

@pytest.fixture
def text_data():
    return TextData([
            [1, 'Superfood', 'Food', '10.00'],
            [2, 'Superwine', 'Wine', '20.00']
        ])

@pytest.fixture
def services_list():
    return [
        Service(1, 'Superfood', 'Food', Decimal('10.00')),
        Service(2, 'Superwine', 'Wine', Decimal('20.00'))
    ]

@pytest.fixture
def service_repo_from_json(json_data):
    return ServiceRepo(json_data)

@pytest.fixture
def service_repo_from_text(text_data):
    return ServiceRepo(text_data)

@pytest.fixture
def service_repo_from_list(services_list):
    return ServiceRepo(services_list)
