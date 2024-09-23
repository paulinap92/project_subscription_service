import pytest
from decimal import Decimal
from myproj.model.user import User, Destination
from myproj.file_repo.file_reader_factory import JsonData, TextData
from myproj.service.service import ServiceRepo
from myproj.service.subscription import SubscriptionRepo
from myproj.service.user import UserRepo, UserService
from myproj.model.service import Service
from myproj.model.subscription import Subscription
from datetime import date

# service expected fixtures
@pytest.fixture
def expected_service_1():
    return Service(1, 'Superfood', 'Food', Decimal('10.00'))

@pytest.fixture
def expected_service_2():
    return Service(2, 'Superwine', 'Wine', Decimal('20.00'))

@pytest.fixture
def expected_service_repo(expected_service_1, expected_service_2):
    return ServiceRepo([expected_service_1, expected_service_2])

#service creation fixtures
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

# expected user fixtures
@pytest.fixture
def expected_user_1():
    return User('Andrés', 'Logroño', Destination.CM, date(1992,12,2), 1)

@pytest.fixture
def expected_user_2():
    return User('Ana', 'Cantó', Destination.IB, date(1988,11,14), 2)

@pytest.fixture
def expected_user_repo(expected_user_1, expected_user_2):
    return UserRepo([expected_user_1, expected_user_2])

# user creation fixtures

@pytest.fixture
def u_json_data():
    return JsonData({
            1: ['Andrés', 'Logroño','CEUTA OR MELILLA TERITORY','1992-12-2', 1],
            2: ['Ana', 'Cantó','BALEARICS ISLANDS','1988-11-14', 2]
        })

@pytest.fixture
def u_text_data():
    return TextData([
            ['Andrés', 'Logroño', 'CEUTA OR MELILLA TERITORY','1992-12-2', 1],
            ['Ana', 'Cantó', 'BALEARICS ISLANDS','1988-11-14', 2]
        ])

@pytest.fixture
def user_list():
    return [
        User('Andrés', 'Logroño', Destination.CM, date(1992,12,2), 1),
        User('Ana', 'Cantó', Destination.IB, date(1988,11,14), 2)
    ]

@pytest.fixture
def user_repo_from_json(u_json_data):
    return UserRepo(u_json_data)

@pytest.fixture
def user_repo_from_text(u_text_data):
    return UserRepo(u_text_data)

@pytest.fixture
def user_repo_from_list(user_list):
    return UserRepo(user_list)


# subscription fixture

@pytest.fixture
def expected_subscription():
    return Subscription(1, 1, 1, Decimal("10.00"), 1, True)
@pytest.fixture
def subscription_list():
    return [
        Subscription(1, 1, 1, Decimal("10.00"), 1, True),
        Subscription(2, 2, 2, Decimal("20.00"), 2, False),
    ]

@pytest.fixture
def subscription_repo_from_list(subscription_list):
    return SubscriptionRepo(subscription_list)

# user service creation fixture
@pytest.fixture
def user_service(service_repo_from_list, subscription_repo_from_list, user_repo_from_list):
    return UserService(user_repo_from_list, service_repo_from_list, subscription_repo_from_list)

