from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Self

@dataclass
class Subscription:
    """
    Represents a subscription for a service by a user.

    Attributes:
        user_id (int): The unique identifier for the user subscribing to the service.
        service_id (int): The unique identifier for the service being subscribed to.
        quantity_per_month (int): The quantity of the service subscribed to per month.
        discount (Decimal | None): The discount applied to the subscription, if any. Defaults to None.
        id_ (int | None): The unique identifier for the subscription. Defaults to None.
        active (bool | None): Indicates whether the subscription is active. Defaults to True.

    Methods:
        get_user_id() -> int:
            Returns the unique identifier of the user.
        get_service_id() -> int:
            Returns the unique identifier of the service.
        is_active() -> bool:
            Returns whether the subscription is currently active.
        set_id(id_: int) -> None:
            Sets the unique identifier for the subscription.
        set_active() -> None:
            Marks the subscription as active.
        set_inactive() -> None:
            Marks the subscription as inactive.
        update(data: dict[str, Any]) -> Self:
            Updates the subscription attributes with the provided data dictionary and returns a new instance.

    Example Usage:
        Creating and updating a `Subscription` instance:

        ```python
        from decimal import Decimal
        from your_module import Subscription

        # Create a new Subscription instance
        subscription = Subscription(
            user_id=123,
            service_id=456,
            quantity_per_month=2,
            discount=Decimal('5.00')
        )

        # Retrieve the user ID
        user_id = subscription.get_user_id()
        print("User ID:", user_id)  # Output: User ID: 123

        # Check if the subscription is active
        is_active = subscription.is_active()
        print("Is Active:", is_active)  # Output: Is Active: True

        # Update the subscription with new data
        updated_subscription = subscription.update({'quantity_per_month': 3, 'discount': Decimal('10.00')})

        print("Updated Subscription:", updated_subscription)
        # Output: Updated Subscription: Subscription(user_id=123, service_id=456, quantity_per_month=3, discount=10.00, id_=None, active=True)
        ```

    Note:
        - The `update` method merges the provided data dictionary with the existing attributes of the `Subscription` instance.
        - The `id_` and `active` attributes can be modified using the `set_id`, `set_active`, and `set_inactive` methods.

    """

    user_id: int
    service_id: int
    quantity_per_month: int
    discount: Decimal | None = None
    id_: int | None = None
    active: bool | None = True

    def get_user_id(self) -> int:
        """
        Returns the unique identifier of the user subscribing to the service.

        Returns:
            int: The user ID.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2)
            subscription.get_user_id()
            # Output: 123
        """
        return self.user_id

    def get_service_id(self) -> int:
        """
        Returns the unique identifier of the service being subscribed to.

        Returns:
            int: The service ID.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2)
            subscription.get_service_id()
            # Output: 456
        """
        return self.service_id

    def is_active(self) -> bool:
        """
        Returns whether the subscription is currently active.

        Returns:
            bool: True if the subscription is active, False otherwise.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2, active=False)
            subscription.is_active()
            # Output: False
        """
        return self.active

    def set_id(self, id_: int) -> None:
        """
        Sets the unique identifier for the subscription.

        Args:
            id_ (int): The unique identifier for the subscription.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2)
            subscription.set_id(789)
            subscription.id_
            # Output: 789
        """
        self.id_ = id_

    def set_active(self) -> None:
        """
        Marks the subscription as active.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2, active=False)
            subscription.set_active()
            subscription.is_active()
            # Output: True
        """
        self.active = True

    def set_inactive(self) -> None:
        """
        Marks the subscription as inactive.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2)
            subscription.set_inactive()
            subscription.is_active()
            # Output: False
        """
        self.active = False

    def update(self, data: dict[str, Any]) -> Self:
        """
        Updates the subscription attributes with the provided data dictionary and returns a new instance
        with the updated attributes.

        Args:
            data (dict[str, Any]): A dictionary containing the attributes to update. Keys should match
                the attribute names of the `Subscription` class.

        Returns:
            Self: A new `Subscription` instance with updated attributes.

        Example:
            subscription = Subscription(user_id=123, service_id=456, quantity_per_month=2)
            updated_subscription = subscription.update({'quantity_per_month': 3, 'discount': Decimal('10.00')})
            updated_subscription
            # Output: Subscription(user_id=123, service_id=456, quantity_per_month=3, discount=10.00, id_=None, active=True)
        """
        updated_data = self.__dict__ | data
        return Subscription(**updated_data)
