from decimal import Decimal
from typing import Any

from myproj.file_repo.file_reader_factory import JsonData, TextData
from myproj.model.service import Service


class ServiceRepo:
    """
    Repository class for managing services.

    This class provides methods to interact with service data, including converting data into `Service` instances,
    retrieving, updating, and deleting services.

    Attributes:
        services (dict): A dictionary of services indexed by their ID.

    Args:
        data (TextData | JsonData | list[Service]):
            The initial data to populate the repository. Can be in the form of `TextData`, `JsonData`, or a list of `Service` instances.
    """

    def __init__(self, data: TextData | JsonData | list[Service]):
        """
        Initializes the ServiceRepo with data and converts it into `Service` instances.

        Args:
            data (TextData | JsonData | list[Service]):
                The data to initialize the repository with.
        """
        self.services = self._data_convert_to_service(data)

    def _data_convert_to_service(self, data: TextData | JsonData | list[Service]) -> dict:
        """
        Converts the provided data into a dictionary of `Service` instances.

        Args:
            data (TextData | JsonData | list[Service]):
                The data to convert.

        Returns:
            dict: A dictionary of `Service` instances indexed by their ID.

        Raises:
            ValueError: If the provided data is of an unsupported type.
        """
        if isinstance(data, JsonData):
            data = data.get_content()
            transformed_data = [Service(int(value[0]), value[1], value[2], Decimal(value[3])) for key, value in data.items()]

        elif isinstance(data, TextData):
            data = data.get_content()
            transformed_data = [Service(int(item[0]), item[1], item[2], Decimal(item[3])) for item in data]

        elif isinstance(data, list) and all(isinstance(item, Service) for item in data):
            transformed_data = data

        else:
            raise ValueError("Unsupported data type")

        return {service.id_: service for service in transformed_data}

    def get_services(self) -> dict:
        """
        Retrieves all services in the repository.

        Returns:
            dict: A dictionary of all `Service` instances indexed by their ID.
        """
        return self.services

    def find_by_id(self, id_: int) -> Service:
        """
        Finds a service by its ID.

        Args:
            id_ (int): The ID of the service to find.

        Returns:
            Service: The `Service` instance with the given ID.

        Raises:
            KeyError: If no service with the specified ID is found.
        """
        found_service = self.services.get(id_)

        if not found_service:
            raise KeyError("Service Not Found")

        return found_service

    def update(self, id_: int, data: dict[str, Any]) -> Service:
        """
        Updates a service with the given ID using the provided data.

        Args:
            id_ (int): The ID of the service to update.
            data (dict[str, Any]): A dictionary containing the updated data.

        Returns:
            Service: The updated `Service` instance.

        Raises:
            KeyError: If no service with the specified ID is found.
        """
        service_to_update = self.find_by_id(id_)
        updated_service = service_to_update.update(data)
        self.services[id_] = updated_service
        return updated_service

    def delete(self, id_: int) -> None:
        """
        Deletes a service with the specified ID.

        Args:
            id_ (int): The ID of the service to delete.

        Raises:
            KeyError: If no service with the specified ID is found.
        """
        if id_ not in self.services:
            raise KeyError(f"Service Not Found")

        self.services.pop(id_)
