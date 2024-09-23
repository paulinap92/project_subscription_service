from myproj.file_repo.file_reader_factory import RegexValidator
import pytest


def test_regex_validator_works_correct():
    regex_validator = RegexValidator(r'^(\d+),([A-Za-z\s]+),([A-Za-z\s]+),(\d+\.\d+)$')
    result_data_validator = regex_validator.validate(['1,Delicious Bites,Food,29.99','2,Vintage Vineyard,Wine,49.99','blablabla'])
    assert ['1,Delicious Bites,Food,29.99','2,Vintage Vineyard,Wine,49.99'] == result_data_validator


def test_regex_validator_no_data_results():
    regex_validator = RegexValidator(r'^(\d+),([A-Za-z\s]+),([A-Za-z\s]+),(\d+\.\d+)$')
    result_data_validator = regex_validator.validate(['blablabla'])
    assert [] == result_data_validator
