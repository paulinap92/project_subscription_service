# Standard library imports
from typing import Any, Final, Type, Self

# Project-specific imports
from myproj.file_repo.file_reader_factory import DataProcessor, DataFormat, FactoryType
from myproj.service.service import ServiceRepo
from myproj.service.subscription import SubscriptionRepo
from myproj.service.user import UserRepo, UserService


def main() -> None:
    """
    Main function to demonstrate the usage of data processing and repository classes.

    It initializes data processors for various data formats and factory types,
    processes data files, and prints out the results for services, subscriptions, and users.
    """

    # File paths for different data formats
    SERVICE_JSON_FILENAME: Final[str] = 'data/data_service.json'
    SERVICE_CSV_FILENAME: Final[str] = 'data/data_service.csv'

    USER_JSON_FILENAME: Final[str] = 'data/data_user.json'
    USER_CSV_FILENAME: Final[str] = 'data/data_user.csv'

    SUBSCRIPTION_JSON_FILENAME: Final[str] = 'data/data_subscription.json'
    SUBSCRIPTION_CSV_FILENAME: Final[str] = 'data/data_subscription.csv'

    # Create DataProcessor instances for different combinations of data format and factory type
    d1 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SERVICE)
    d2 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SERVICE)
    d3 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_USER)
    d4 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_USER)
    d5 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SUBSCRIPTION)
    d6 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SUBSCRIPTION)

    # Demonstrate invalid processor creation
    print('eee')
    print(DataProcessor.create_processor("invalid_data_type", "invalid_factory_type"))

    # Create and use ServiceRepo with processed data
    s1 = ServiceRepo(d1.process(SERVICE_CSV_FILENAME))
    print(s1.get_services())

    s2 = ServiceRepo(d2.process(SERVICE_JSON_FILENAME))
    print(s2.get_services())

    # Create and use SubscriptionRepo with processed data
    ss1 = SubscriptionRepo(d5.process(SUBSCRIPTION_CSV_FILENAME))
    print(ss1.get_subscriptions())

    ss2 = SubscriptionRepo(d6.process(SUBSCRIPTION_JSON_FILENAME))
    print(ss2.get_subscriptions())

    # Create and use UserRepo with processed data
    u1 = UserRepo(d3.process(USER_CSV_FILENAME))
    print(u1.get_all_users())

    u2 = UserRepo(d4.process(USER_JSON_FILENAME))
    print(u2.get_all_users())

    # Print subscriptions by user ID and service ID
    print(ss1.get_subscriptions_by_user_id(1))
    print(ss1.get_subscriptions_by_service_id(2))

    # Create UserService and perform operations
    user_service = UserService(u1, s1, ss1)
    print(user_service.subscribe_user_to_service(10, 11, 1))
    print(user_service.active_subscriptions_report())


if __name__ == '__main__':
    main()


