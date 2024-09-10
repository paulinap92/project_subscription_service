"""
Module for data processing including loading, validating, converting, and handling different data formats.
Uses abstract factory pattern to implement data processing for different data formats.

 Example:
        To process data from different file formats using various factory types, follow the example below:

        ´´´python
        from myproj.file_repo.file_reader_factory import DataProcessor, DataFormat, FactoryType

        # File paths for different types of data
        SERVICE_TEXT_FILENAME = 'data/data_service.txt'

        # Create a DataProcessor instance for TEXT format with the FROM_SERVICE factory type
        d1 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SERVICE)

        # Process service data in TXT format
        processed_data_service_txt = d1.process(SERVICE_TEXT_FILENAME)

        # Output: processed and validated data in TextData format
        print("Processed Data (TextData):", processed_data_service_txt)

        **Expected Output:**
        The `processed_data_service_txt` should be an instance of `TextData` containing the processed
        and validated content from the text file. For example:

        TextData(content=[
            ['1', 'Delicious Bites', 'Food', '29.99'],
            ['2', 'Vintage Vineyard', 'Wine', '49.99']
        ])
       ```
"""

import json
import re

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Self

from dataclasses import dataclass

# ------------------
# ENUM
# ------------------

class DataFormat(Enum):
    """
    Enum for specifying the data format.

    Attributes:
        JSON: Represents JSON data format.
        TEXT: Represents plain text data format.
    """
    JSON = 'JSON'
    TEXT = 'TEXT'

class FactoryType(Enum):
    """
    Enum for specifying the factory type.

    Attributes:
        FROM_SERVICE: Represents data from a service.
        FROM_USER: Represents data from a user.
        FROM_SUBSCRIPTION: Represents data from a subscription.
    """
    FROM_SERVICE = 'FROM_SERVICE'
    FROM_USER = 'FROM_USER'
    FROM_SUBSCRIPTION = 'FROM_SUBSCRIPTION'

class RegexPatterns(Enum):
    """
    Enum for storing regex patterns for different data types.

    Attributes:
        FROM_SERVICE: Regex pattern for service data.
        FROM_USER: Regex pattern for user data.
        FROM_SUBSCRIPTION: Regex pattern for subscription data.
    """
    FROM_SERVICE = r'^(\d+),([A-Za-z\s]+),([A-Za-z\s]+),(\d+\.\d+)$'
    FROM_USER = (r'^([A-Za-ząćęłńóśźżÁÉÍÓÚÜÑáéíóúüñĄĆĘŁŃÓŚŹŻ]+),([A-Za-ząćęłńóśźżÁÉÍÓÚÜÑáéíóúüñĄĆĘŁŃÓŚŹŻ]+),'
                 r'([A-Z ]+),(\d{4}-\d{2}-\d{2}),(\d+)$')
    FROM_SUBSCRIPTION = r'^(\d+,\d+,\d+,\d+,\d+,\d)$'

# -----------------------------------------------------------
# MODEL
# -----------------------------------------------------------

@dataclass
class TextData:
    """
    Data class for handling text data.

    Attributes:
        content: A list of lists containing strings representing the text data.

    Methods:
        get_content: Returns the content of the text data.
    """
    content: list[list[str]]

    def get_content(self) -> list[list[str]]:
        """
        Returns the content of the text data.

        Returns:
            A list of lists containing strings representing the text data.
        """
        return self.content

@dataclass
class JsonData:
    """
    Data class for handling JSON data.

    Attributes:
        data: A dictionary where keys are integers and values are lists of strings representing the JSON data.

    Methods:
        get_content: Returns the content of the JSON data.
    """
    data: dict[int, list[str]]

    def get_content(self) -> dict[int, list[str]]:
        """
        Returns the content of the JSON data.

        Returns:
            A dictionary where keys are integers and values are lists of strings representing the JSON data.
        """
        return self.data

# -----------------------------------------------------------
# LOADER
# -----------------------------------------------------------

class DataLoader(ABC):
    """
    Abstract base class for data loaders.

    Methods:
        load: Abstract method to load data from a given path.
    """
    @abstractmethod
    def load(self, path: str) -> list[str]:
        """
        Abstract method to load data from a given path.

        Args:
            path: The path to the data file.

        Returns:
            A list of strings representing the loaded data.
        """
        pass            # pragma: no cover

class JsonDataLoader(DataLoader):
    """
    Data loader for JSON files.

    Methods:
        load: Loads data from a JSON file.
    """
    def load(self, path: str) -> list[str]:
        """
        Loads data from a JSON file.

        Args:
            path: The path to the JSON file.

        Returns:
            A list of strings representing the loaded data.

        Raises:
            AttributeError: If the file does not have a '.json' extension.
            FileNotFoundError: If the file is not found.
        """
        if not path.endswith('json'):
            raise AttributeError('File has incorrect extension')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return [','.join(map(str, (item.values()))) for item in json.load(f)]
        except Exception as e:
            raise FileNotFoundError(f'File not found: {e}')

class TextDataLoader(DataLoader):
    """
    Data loader for text files.

    Methods:
        load: Loads data from a text file.
    """
    def load(self, path: str) -> list[str]:
        """
        Loads data from a text file.

        Args:
            path: The path to the text file.

        Returns:
            A list of strings representing the loaded data.

        Raises:
            AttributeError: If the file does not have a '.csv' or '.txt' extension.
            FileNotFoundError: If the file is not found.
        """
        if not (path.endswith('csv') or path.endswith('txt')):
            raise AttributeError('File has incorrect extension')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return [re.sub(r'\n', '', line) for line in f.readlines()][1:]
        except Exception as e:
            raise FileNotFoundError(f'File not found: {e}')

# -----------------------------------------------------------
# VALIDATOR
# -----------------------------------------------------------

class Validator(ABC):
    """
    Abstract base class for data validators.

    Methods:
        validate: Abstract method to validate data.
    """
    @abstractmethod
    def validate(self, data: list[str]) -> list[str]:
        """
        Abstract method to validate data.

        Args:
            data: A list of strings representing the data to be validated.

        Returns:
            A list of strings representing the validated data.
        """
        pass            # pragma: no cover

@dataclass
class RegexValidator(Validator):
    """
    Validator class using regular expressions.

    Attributes:
        regex: The regular expression pattern used for validation.

    Methods:
        validate: Validates data using the provided regular expression.
    """
    regex: str = None

    def validate(self, data: list[str]) -> list[str]:
        """
        Validates data using the provided regular expression.

        Args:
            data: A list of strings representing the data to be validated.

        Returns:
            A list of strings that match the regular expression.
        """
        return [d for d in data if re.match(self.regex, d) is not None]

# -----------------------------------------------------------
# CONVERTER
# -----------------------------------------------------------

class Converter(ABC):
    """
    Abstract base class for data converters.

    Methods:
        convert: Abstract method to convert data.
    """
    @abstractmethod
    def convert(self, data: list[str]) -> Any:
        """
        Abstract method to convert data.

        Args:
            data: A list of strings representing the data to be converted.

        Returns:
            The converted data in the specified format.
        """
        pass    # pragma: no cover

class ToTextDataConverter(Converter):
    """
    Converter class to convert data to TextData format.

    Methods:
        convert: Converts data to TextData format.
    """
    def convert(self, data: list[str]) -> TextData:
        """
        Converts data to TextData format.

        Args:
            data: A list of strings representing the data to be converted.

        Returns:
            An instance of TextData containing the converted data.
        """
        transformed_data = [item.split(',') for item in data]
        return TextData(transformed_data)

class ToJsonDataConverter(Converter):
    """
    Converter class to convert data to JsonData format.

    Methods:
        convert: Converts data to JsonData format.
    """
    def convert(self, data: list[str]) -> JsonData:
        """
        Converts data to JsonData format.

        Args:
            data: A list of strings representing the data to be converted.

        Returns:
            An instance of JsonData containing the converted data.
        """
        transformed_data = [item.split(',') for item in data]
        return JsonData(dict([(i, v) for i, v in enumerate(transformed_data)]))

# -----------------------------------------------------------
# FACTORY
# -----------------------------------------------------------

class DataFactory(ABC):
    """
    Abstract base class for data factories.

    Methods:
        create_data_loader: Abstract method to create a data loader.
        create_validator: Abstract method to create a data validator.
        create_converter: Abstract method to create a data converter.
    """
    @abstractmethod
    def create_data_loader(self) -> DataLoader:
        """
        Abstract method to create a data loader.

        Returns:
            An instance of a DataLoader.
        """
        pass    # pragma: no cover

    @abstractmethod
    def create_validator(self) -> Validator:
        """
        Abstract method to create a data validator.

        Returns:
            An instance of a Validator.
        """
        pass    # pragma: no cover

    @abstractmethod
    def create_converter(self) -> Converter:
        """
        Abstract method to create a data converter.

        Returns:
            An instance of a Converter.
        """
        pass    # pragma: no cover

@dataclass
class FromJsonFileToJsonDataWithExpectedRegexDataFactory(DataFactory):
    """
    Factory class to handle JSON data files and validate them using regex.

    Attributes:
        regex: The regular expression pattern used for validation.
    """
    regex: str

    def create_data_loader(self) -> DataLoader:
        """
        Creates a JSON data loader.

        Returns:
            An instance of JsonDataLoader.
        """
        return JsonDataLoader()

    def create_validator(self) -> Validator:
        """
        Creates a regex validator.

        Returns:
            An instance of RegexValidator with the specified regex.
        """
        return RegexValidator(self.regex)

    def create_converter(self) -> Converter:
        """
        Creates a JSON data converter.

        Returns:
            An instance of ToJsonDataConverter.
        """
        return ToJsonDataConverter()

@dataclass
class FromTextFileToTextDataWithExpectedRegexDataFactory(DataFactory):
    """
    Factory class to handle text data files and validate them using regex.

    Attributes:
        regex: The regular expression pattern used for validation.
    """
    regex: str

    def create_data_loader(self) -> DataLoader:
        """
        Creates a text data loader.

        Returns:
            An instance of TextDataLoader.
        """
        return TextDataLoader()

    def create_validator(self) -> Validator:
        """
        Creates a regex validator.

        Returns:
            An instance of RegexValidator with the specified regex.
        """
        return RegexValidator(self.regex)

    def create_converter(self) -> Converter:
        """
        Creates a text data converter.

        Returns:
            An instance of ToTextDataConverter.
        """
        return ToTextDataConverter()

class DataProcessor:
    """
    Class to process data using a specified factory.

    Attributes:
        data_loader: An instance of DataLoader.
        validator: An instance of Validator.
        converter: An instance of Converter.

    Methods:
        process: Processes data from the given path.
        create_processor: Creates a data processor based on the data type and factory type.
    """
    def __init__(self, data_factory: DataFactory):
        """
        Initializes the DataProcessor with a specified factory.

        Args:
            data_factory: An instance of DataFactory to create data loader, validator, and converter.
        """
        self.data_loader = data_factory.create_data_loader()
        self.validator = data_factory.create_validator()
        self.converter = data_factory.create_converter()

    def process(self, path: str = None) -> Any:
        """
        Processes data from the given path.

        Args:
            path: The path to the data file.

        Returns:
            The processed data in the specified format.

        Raises:
            Any exceptions raised by the data loader, validator, or converter.
        """
        loaded_data = self.data_loader.load(path)
        validated_data = self.validator.validate(loaded_data)
        return self.converter.convert(validated_data)

    @classmethod
    def create_processor(cls, data_type: Enum, factory_type: Enum) -> Self:
        """
        Creates a data processor based on the data type and factory type.

        Args:
            data_type: An instance of DataFormat specifying the data format.
            factory_type: An instance of FactoryType specifying the factory type.

        Returns:
            An instance of DataProcessor configured with the appropriate factory.
        """
        match data_type, factory_type:
            case DataFormat.JSON, FactoryType.FROM_SERVICE:
                return cls(FromJsonFileToJsonDataWithExpectedRegexDataFactory(RegexPatterns.FROM_SERVICE.value))
            case DataFormat.JSON, FactoryType.FROM_USER:
                return cls(FromJsonFileToJsonDataWithExpectedRegexDataFactory(RegexPatterns.FROM_USER.value))
            case DataFormat.JSON, FactoryType.FROM_SUBSCRIPTION:
                return cls(FromJsonFileToJsonDataWithExpectedRegexDataFactory(RegexPatterns.FROM_SUBSCRIPTION.value))
            case DataFormat.TEXT, FactoryType.FROM_SERVICE:
                return cls(FromTextFileToTextDataWithExpectedRegexDataFactory(RegexPatterns.FROM_SERVICE.value))
            case DataFormat.TEXT, FactoryType.FROM_USER:
                return cls(FromTextFileToTextDataWithExpectedRegexDataFactory(RegexPatterns.FROM_USER.value))
            case DataFormat.TEXT, FactoryType.FROM_SUBSCRIPTION:
                return cls(FromTextFileToTextDataWithExpectedRegexDataFactory(RegexPatterns.FROM_SUBSCRIPTION.value))
