from dataclasses import dataclass
from datetime import date
from enum import Enum


class Destination(Enum):
    """
    Enumeration representing destinations within Spain.

    Attributes:
        PN (str): Represents the Peninsula destination.
        IB (str): Represents the Balearic Islands destination.
        IC (str): Represents the Canary Islands destination.
        CM (str): Represents the Ceuta or Melilla territory destination.
    """

    PN = 'PENINSULA'
    IB = 'BALEARICS ISLANDS'
    IC = 'CANARY ISLANDS'
    CM = 'CEUTA OR MELILLA TERITORY'

@dataclass(frozen=True)
class User:
    """
    Represents a user with basic information.

    Attributes:
        name (str): The first name of the user.
        surname (str): The last name of the user.
        origin (Destination): The origin of the user, represented by a `Destination` enum.
        birthdate (date): The birthdate of the user.
        id_ (int | None): The optional user ID.

    Methods:
        get_id() -> int | None:
            Returns the ID of the user.

        is_older_than(age_min: int) -> bool:
            Checks if the user is older than a specified minimum age.

    Example:
        Creating and using a `User` instance:

        ```python
        from datetime import date
        from your_module import User, Destination

        # Create a new User instance
        user = User(
            name="John",
            surname="Doe",
            origin=Destination.PN,
            birthdate=date(1990, 1, 1)
        )

        # Retrieve the user ID
        user_id = user.get_id()
        print("User ID:", user_id)  # Output: User ID: None

        # Check if the user is older than 30
        is_older = user.is_older_than(30)
        print("Is older than 30:", is_older)  # Output: Is older than 30: True
        ```
    """
    name: str
    surname: str
    origin: Destination
    birthdate: date
    id_: int | None = None

    def get_id(self):
        """
        Returns the ID of the user.

        Returns:
            int | None: The ID of the user, or None if not set.

        Example:
            >>> user = User(name="John", surname="Doe", origin=Destination.PN, birthdate=date(1990, 1, 1))
            >>> user.get_id()
            None
        """
        return self.id_

    def is_older_than(self, age_min: int) -> bool:
        """
        Checks if the user is older than a specified minimum age.

        Args:
            age_min (int): The minimum age to check against.

        Returns:
            bool: True if the user is older than the specified minimum age, False otherwise.

        Raises:
            ValueError: If the provided age_min is not within the valid range (0 to 150).

        Example:
            user = User(name="John", surname="Doe", origin=Destination.PN, birthdate=date(1990, 1, 1))
            user.is_older_than(30)
            True
        """
        if age_min < 0 or age_min > 150:
            raise ValueError("Age value not correct")

        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age >= age_min
