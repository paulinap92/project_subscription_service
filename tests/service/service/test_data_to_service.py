from myproj.service.service import ServiceRepo
from myproj.file_repo.file_reader_factory import JsonData, TextData
from decimal import Decimal
import unittest

import pytest


def test_not_correct_data_to_service():
    with pytest.raises(ValueError) as e:
        s = ServiceRepo('fake_service')
    assert str(e.value).startswith('Unsupported')


def test_data_convert_to_service_from_json(service_repo_from_json, expected_service_repo):
    services = service_repo_from_json.get_services()
    assert len(services) == 2
    assert services == expected_service_repo.get_services()


def test_data_convert_to_service_from_text(service_repo_from_text, expected_service_repo):
    services = service_repo_from_text.get_services()
    assert len(services) == 2
    assert services == expected_service_repo.get_services()


def test_data_convert_to_service_from_list(service_repo_from_list, expected_service_repo):
    services = service_repo_from_list.get_services()
    assert len(services) == 2
    assert services == expected_service_repo.get_services()





