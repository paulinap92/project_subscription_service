from decimal import Decimal
from typing import Any

from myproj.file_repo.file_reader_factory import TextData, JsonData
from myproj.model.subscription import Subscription

class SubscriptionRepo:
    """
    Repository class for managing subscriptions.

    This class provides methods to interact with subscription data, including converting data into `Subscription` instances,
    retrieving, updating, adding, and deleting subscriptions.

    Attributes:
        subscriptions (dict): A dictionary of subscriptions indexed by their ID.

    Args:
        data (TextData | JsonData | list[Subscription]):
            The initial data to populate the repository. Can be in the form of `TextData`, `JsonData`, or a list of `Subscription` instances.
    """

    def __init__(self, data: TextData | JsonData | list[Subscription]):
        """
        Initializes the SubscriptionRepo with data and converts it into `Subscription` instances.

        Args:
            data (TextData | JsonData | list[Subscription]):
                The data to initialize the repository with.
        """
        self.subscriptions = self._data_convert_to_subscription(data)

    def _data_convert_to_subscription(self, data: TextData | JsonData | list[Subscription]) -> dict:
        """
        Converts the provided data into a dictionary of `Subscription` instances.

        Args:
            data (TextData | JsonData | list[Subscription]):
                The data to convert.

        Returns:
            dict: A dictionary of `Subscription` instances indexed by their ID.

        Raises:
            ValueError: If the provided data is of an unsupported type.
        """
        if isinstance(data, JsonData):
            data = data.get_content()
            transformed_data = [
                Subscription(
                    int(value[0]),
                    int(value[1]),
                    int(value[2]),
                    Decimal(value[3]),
                    int(value[-2]),
                    bool(int(value[-1]))
                )
                for key, value in data.items()
            ]

        elif isinstance(data, TextData):
            data = data.get_content()
            transformed_data = [
                Subscription(
                    int(item[0]),
                    int(item[1]),
                    int(item[2]),
                    Decimal(item[3]),
                    int(item[-2]),
                    bool(int(item[-1]))
                )
                for item in data
            ]

        elif isinstance(data, list) and all(isinstance(item, Subscription) for item in data):
            transformed_data = data

        else:
            raise ValueError("Unsupported data type")

        return {subscription.id_: subscription for subscription in transformed_data}

    def get_subscriptions(self) -> dict:
        """
        Retrieves all subscriptions in the repository.

        Returns:
            dict: A dictionary of all `Subscription` instances indexed by their ID.
        """
        return self.subscriptions

    def find_by_id(self, id_: int) -> Subscription:
        """
        Finds a subscription by its ID.

        Args:
            id_ (int): The ID of the subscription to find.

        Returns:
            Subscription: The `Subscription` instance with the given ID.

        Raises:
            KeyError: If no subscription with the specified ID is found.
        """
        found_subscription = self.subscriptions.get(id_)

        if not found_subscription:
            raise KeyError("Subscription Not Found")

        return found_subscription

    def add_subscription(self, data: dict[str, Any] | Subscription) -> Subscription:
        """
        Adds a new subscription to the repository.

        Args:
            data (dict[str, Any] | Subscription): The data to create the new subscription.
                Can be a dictionary of subscription attributes or a `Subscription` instance.

        Returns:
            Subscription: The newly added `Subscription` instance.
        """
        subscription_id = len(self.subscriptions) + 1

        if isinstance(data, Subscription):
            subscription_data = data
            subscription_data.set_id(subscription_id)
        else:
            data['id_'] = subscription_id
            subscription_data = Subscription(**data)

        self.subscriptions[subscription_data.id_] = subscription_data
        return subscription_data

    def get_subscriptions_by_user_id(self, user_id: int) -> list[Subscription]:
        """
        Retrieves all subscriptions for a specific user.

        Args:
            user_id (int): The user ID to filter subscriptions.

        Returns:
            list[Subscription]: A list of `Subscription` instances associated with the given user ID.
        """
        return [value for key, value in self.subscriptions.items() if value.get_user_id() == user_id]

    def get_subscriptions_by_service_id(self, service_id: int) -> list[Subscription]:
        """
        Retrieves all subscriptions for a specific service.

        Args:
            service_id (int): The service ID to filter subscriptions.

        Returns:
            list[Subscription]: A list of `Subscription` instances associated with the given service ID.
        """
        return [value for key, value in self.subscriptions.items() if value.get_service_id() == service_id]

    def get_all_subscriptions(self) -> list[Subscription]:
        """
        Retrieves all subscriptions in the repository.

        Returns:
            list[Subscription]: A list of all `Subscription` instances.
        """
        return list(self.subscriptions.values())

    def get_all_active_subscriptions(self) -> list[Subscription]:
        """
        Retrieves all active subscriptions in the repository.

        Returns:
            list[Subscription]: A list of all active `Subscription` instances.
        """
        return [value for value in self.subscriptions.values() if value.is_active()]

    def update(self, id_: int, data: dict[str, Any]) -> Subscription:
        """
        Updates an existing subscription with the provided data.

        Args:
            id_ (int): The ID of the subscription to update.
            data (dict[str, Any]): A dictionary containing the updated data.

        Returns:
            Subscription: The updated `Subscription` instance.

        Raises:
            KeyError: If no subscription with the specified ID is found.
        """
        subscription_to_update = self.find_by_id(id_)
        updated_subscription = subscription_to_update.update(data)
        self.subscriptions[id_] = updated_subscription
        return updated_subscription

    def delete(self, id_: int) -> None:
        """
        Deletes a subscription by its ID.

        Args:
            id_ (int): The ID of the subscription to delete.

        Raises:
            KeyError: If no subscription with the specified ID is found.
        """
        if id_ not in self.subscriptions:
            raise KeyError("Subscription Not Found")

        self.subscriptions.pop(id_)
