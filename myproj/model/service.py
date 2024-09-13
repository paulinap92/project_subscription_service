from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Self


@dataclass
class Service:
    """
    Represents a service with attributes including ID, name, category, and price.

    Attributes:
        id_ (int): The unique identifier for the service.
        name (str): The name of the service.
        category (str): The category to which the service belongs.
        price (Decimal): The price of the service.

    Methods:
        get_id() -> int:
            Returns the unique identifier of the service.
        update(data: dict[str, Any]) -> Self:
            Updates the service attributes with the given data dictionary and returns a new instance.

    Example Usage:
        Creating and updating a `Service` instance for food-related services:

        ```python
        from decimal import Decimal
        from your_module import Service

        # Create a new Service instance for a food service
        service = Service(id_=1, name='Gourmet Burger', category='Burgers', price=Decimal('12.99'))

        # Retrieve the ID
        service_id = service.get_id()
        print("Service ID:", service_id)
        # Output: Service ID: 1

        # Update the service with new data
        updated_service = service.update({'name': 'Deluxe Burger', 'price': Decimal('14.99')})

        print("Updated Service:", updated_service)
        # Output: Updated Service: Service(id_=1, name='Deluxe Burger', category='Burgers', price=14.99)
        ```

    """

    id_: int
    name: str
    category: str
    price: Decimal

    def get_id(self) -> int:
        """
        Returns the unique identifier of the service.

        Returns:
            int: The ID of the service.

        Example:
            service = Service(id_=1, name='Gourmet Burger', category='Burgers', price=Decimal('12.99'))
            service.get_id()
            # Output: 1
        """
        return self.id_

    def update(self, data: dict[str, Any]) -> Self:
        """
        Updates the food service attributes with the provided data dictionary and returns a new instance
        with the updated attributes.

        Args:
            data (dict[str, Any]): A dictionary containing the attributes to update. Keys should match
                the attribute names of the `Service` class.

        Returns:
            Self: A new `Service` instance with updated attributes.

        Example:
            service = Service(id_=1, name='Gourmet Burger', category='Burgers', price=Decimal('12.99'))
            updated_service = service.update({'name': 'Deluxe Burger', 'price': Decimal('14.99')})
            updated_service
            # Output: Service(id_=1, name='Deluxe Burger', category='Burgers', price=Decimal('14.99'))
        """
        updated_data = self.__dict__ | data
        return Service(**updated_data)
