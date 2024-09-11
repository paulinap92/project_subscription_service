from unittest.mock import MagicMock, patch
from myproj.file_repo.file_reader_factory import DataFactory, \
    DataProcessor, \
    TextDataLoader, \
    RegexValidator, \
    ToTextDataConverter, \
    DataLoader, \
    Validator, \
    Converter, \
    DataFormat, \
    FactoryType, \
    RegexPatterns

import pytest
import logging

class MockDataFactory(DataFactory):
    def create_data_loader(self) -> DataLoader:
        text_data_loader = TextDataLoader()
        text_data_loader.load = MagicMock(return_value=['Alejandro,García,PENINSULA,1990-05-12,1','123,Pedro,2022,Madrid'])
        return text_data_loader

    def create_validator(self) -> Validator:
        regex_validator = RegexValidator()
        regex_validator.validate = MagicMock(return_value=['Alejandro,García,PENINSULA,1990-05-12,1'])
        return regex_validator

    def create_converter(self) -> Converter:
        to_text_data_converter = ToTextDataConverter()
        to_text_data_converter.convert = MagicMock(return_value=['Alejandro','García','PENINSULA','1990-05-12,1'])
        return to_text_data_converter


def test_when_data_processor_works_correct():
    data_processor = DataProcessor(MockDataFactory())
    assert ['Alejandro','García','PENINSULA','1990-05-12,1'] == data_processor.process()


@patch('myproj.file_repo.file_reader_factory.FromJsonFileToJsonDataWithExpectedRegexDataFactory')
def test_create_processor_json_from_service(mock_json_factory):
    processor = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SERVICE)

    assert isinstance(processor, DataProcessor)
    mock_json_factory.assert_called_once_with(RegexPatterns.FROM_SERVICE.value)


@patch('myproj.file_repo.file_reader_factory.FromTextFileToTextDataWithExpectedRegexDataFactory')
def test_create_processor_text_from_user(mock_text_factory):
    processor = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_USER)

    assert isinstance(processor, DataProcessor)
    mock_text_factory.assert_called_once_with(RegexPatterns.FROM_USER.value)

@patch('myproj.file_repo.file_reader_factory.FromJsonFileToJsonDataWithExpectedRegexDataFactory')
def test_create_processor_json_from_subscription(mock_json_factory):
    processor = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SUBSCRIPTION)

    assert isinstance(processor, DataProcessor)
    mock_json_factory.assert_called_once_with(RegexPatterns.FROM_SUBSCRIPTION.value)

@patch('myproj.file_repo.file_reader_factory.FromJsonFileToJsonDataWithExpectedRegexDataFactory')
def test_create_processor_json_from_user(mock_json_factory):
    processor = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_USER)

    assert isinstance(processor, DataProcessor)
    mock_json_factory.assert_called_once_with(RegexPatterns.FROM_USER.value)


@patch('myproj.file_repo.file_reader_factory.FromTextFileToTextDataWithExpectedRegexDataFactory')
def test_create_processor_text_from_service(mock_text_factory):
    processor = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SERVICE)

    assert isinstance(processor, DataProcessor)
    mock_text_factory.assert_called_once_with(RegexPatterns.FROM_SERVICE.value)

@patch('myproj.file_repo.file_reader_factory.FromTextFileToTextDataWithExpectedRegexDataFactory')
def test_create_processor_text_from_subscription(mock_text_factory):
    processor = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SUBSCRIPTION)

    assert isinstance(processor, DataProcessor)
    mock_text_factory.assert_called_once_with(RegexPatterns.FROM_SUBSCRIPTION.value)

def test_create_processor_invalid_combination():

    assert (DataProcessor.create_processor("invalid_data_type", "invalid_factory_type")) == None