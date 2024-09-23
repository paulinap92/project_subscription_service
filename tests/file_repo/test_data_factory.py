from myproj.file_repo.file_reader_factory import FromTextFileToTextDataWithExpectedRegexDataFactory, \
    FromJsonFileToJsonDataWithExpectedRegexDataFactory, DataLoader, Validator, Converter
import pytest


def test_text_data_factory():
    data_factory = FromTextFileToTextDataWithExpectedRegexDataFactory(r'\d')
    loader = data_factory.create_data_loader()
    validator = data_factory.create_validator()
    converter = data_factory.create_converter()
    assert isinstance(loader, DataLoader)
    assert isinstance(validator, Validator)
    assert isinstance(converter, Converter)


def test_json_data_factory():
    data_factory = FromJsonFileToJsonDataWithExpectedRegexDataFactory(r'\d')
    loader = data_factory.create_data_loader()
    validator = data_factory.create_validator()
    converter = data_factory.create_converter()
    assert isinstance(loader, DataLoader)
    assert isinstance(validator, Validator)
    assert isinstance(converter, Converter)
