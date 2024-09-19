from datetime import date, datetime
from decimal import Decimal
from dataclasses import dataclass

from myproj.file_repo.file_reader_factory import TextData, JsonData
from myproj.model.subscription import Subscription
from myproj.model.user import User, Destination
from myproj.service.service import ServiceRepo
from myproj.service.subscription import SubscriptionRepo


class UserRepo:
    """
    Repository for managing user data.

    Args:
        data (TextData | JsonData | list[User]): The data source for user information, which can be
            a TextData or JsonData instance or a list of User instances.

    Attributes:
        users (dict): A dictionary mapping user IDs to User objects.

    Methods:
        get_all_users() -> dict:
            Returns all users in the repository.

        find_by_id(id_: int) -> User:
            Retrieves a user by their ID.

        get_users_older_than(age_min: int) -> list[User]:
            Returns a list of users older than a specified minimum age.

        delete(id_: int) -> None:
            Deletes a user by their ID.
    """

    def __init__(self, data: TextData | JsonData | list[User]):
        self.users = self._data_convert_to_user(data)

    def _data_convert_to_user(self, data: TextData | JsonData | list[User]) -> dict:
        """
        Converts raw data into a dictionary of User objects.

        Args:
            data (TextData | JsonData | list[User]): The data source to convert.

        Returns:
            dict: A dictionary mapping user IDs to User objects.

        Raises:
            ValueError: If the data type is unsupported.
        """
        if isinstance(data, JsonData):
            data = data.get_content()
            transformed_data = [User(value[0], value[1], Destination(value[2]),
                                     datetime.strptime(value[3], "%Y-%m-%d").date(),
                                     int(value[-1])) for key, value in data.items()]
        elif isinstance(data, TextData):
            data = data.get_content()
            transformed_data = [User(item[0], item[1], Destination(item[2]),
                                     datetime.strptime(item[3], "%Y-%m-%d").date(),
                                     int(item[-1])) for item in data]
        elif isinstance(data, list) and all(isinstance(item, User) for item in data):
            transformed_data = data
        else:
            raise ValueError("Unsupported data type")

        return {user.id_: user for user in transformed_data}

    def get_all_users(self) -> dict:
        """
        Returns all users in the repository.

        Returns:
            dict: A dictionary mapping user IDs to User objects.
        """
        return self.users

    def find_by_id(self, id_: int) -> User:
        """
        Retrieves a user by their ID.

        Args:
            id_ (int): The ID of the user to retrieve.

        Returns:
            User: The user with the specified ID.

        Raises:
            KeyError: If the user is not found.
        """
        found_user = self.users.get(id_)

        if not found_user:
            raise KeyError("User Not Found")

        return found_user

    def get_users_older_than(self, age_min: int) -> list[User]:
        """
        Returns a list of users older than a specified minimum age.

        Args:
            age_min (int): The minimum age to filter users.

        Returns:
            list[User]: A list of users older than the specified minimum age.
        """
        return [user for user in self.users.values() if user.is_older_than(age_min)]

    def delete(self, id_: int) -> None:
        """
        Deletes a user by their ID.

        Args:
            id_ (int): The ID of the user to delete.

        Raises:
            KeyError: If the user is not found.
        """
        if id_ not in self.users:
            raise KeyError("User Not Found")
        self.users.pop(id_)


@dataclass
class UserService:
    """
    Service for managing user-related operations and subscriptions.

    Args:
        user_repo (UserRepo): The repository for managing user data.
        service_repo (ServiceRepo): The repository for managing service data.
        subscription_repo (SubscriptionRepo): The repository for managing subscription data.

    Methods:
        subscriptions_for_user_id(user_id: int) -> list[Subscription]:
            Retrieves all subscriptions for a given user ID.

        users_subscribed_to_service(service_id: int) -> list[User]:
            Retrieves all users subscribed to a given service ID.

        subscribe_user_to_service(user_id: int, service_id: int, quantity_per_month: int, discount: Decimal = None) -> Subscription:
            Subscribes a user to a service with specified quantity and optional discount.

        active_subscriptions_report() -> dict:
            Generates a report of active subscriptions, mapping users to their subscribed services.
    """

    user_repo: UserRepo
    service_repo: ServiceRepo
    subscription_repo: SubscriptionRepo

    def subscriptions_for_user_id(self, user_id: int) -> list[Subscription]:
        """
        Retrieves all subscriptions for a given user ID.

        Args:
            user_id (int): The ID of the user to retrieve subscriptions for.

        Returns:
            list[Subscription]: A list of subscriptions for the specified user ID.
        """
        subscriptions = self.subscription_repo.get_subscriptions_by_user_id(user_id)
        return subscriptions

    def users_subscribed_to_service(self, service_id: int) -> list[User]:
        """
        Retrieves all users subscribed to a given service ID.

        Args:
            service_id (int): The ID of the service to find users for.

        Returns:
            list[User]: A list of users subscribed to the specified service ID.
        """
        subscriptions = self.subscription_repo.get_subscriptions_by_service_id(service_id)
        users = [self.user_repo.find_by_id(subscription.user_id) for subscription in subscriptions]
        return users

    def subscribe_user_to_service(self, user_id: int, service_id: int, quantity_per_month: int,
                                  discount: Decimal = None) -> Subscription:
        """
        Subscribes a user to a service with specified quantity and optional discount.

        Args:
            user_id (int): The ID of the user to subscribe.
            service_id (int): The ID of the service to subscribe to.
            quantity_per_month (int): The quantity of the service per month.
            discount (Decimal, optional): An optional discount for the subscription.

        Returns:
            Subscription: The created subscription.
        """
        user = self.user_repo.find_by_id(user_id)
        service = self.service_repo.find_by_id(service_id)
        subscription = Subscription(user.get_id(), service.get_id(), quantity_per_month, discount)
        self.subscription_repo.add_subscription(subscription)
        return subscription

    def active_subscriptions_report(self) -> dict:
        """
        Generates a report of active subscriptions, mapping users to their subscribed services.

        Returns:
            dict: A dictionary where keys are User objects and values are lists of Service objects
                  representing the active subscriptions for each user.
        """
        subscriptions = self.subscription_repo.get_all_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.is_active()]
        report = {}
        for sub in active_subscriptions:
            user = self.user_repo.find_by_id(sub.user_id)
            service = self.service_repo.find_by_id(sub.service_id)
            report.setdefault(user, []).append(service)
        return report
