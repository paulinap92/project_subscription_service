import pytest


@pytest.fixture
def bad_extension_path():
    return 'data/data_test/test_bad_extension.xml'


@pytest.fixture
def empty_csv_file_path():
    return 'data/data_test/test_empty.csv'


@pytest.fixture
def empty_json_file_path():
    return 'data/data_test/test_empty.json'


@pytest.fixture
def good_csv_file_path():
    return 'data/data_test/test_service.csv'


@pytest.fixture
def good_json_file_path():
    return 'data/data_test/test_service.json'
