# Subscription Management Service


## Project Overview

The Subscription Management Service (SMS) is designed to facilitate the management of user subscriptions to various services. The system supports reading data from both JSON and text files, leveraging the Abstract Factory design pattern to handle different file formats. Users can subscribe to services and generate reports on their subscriptions.

## Project Assumptions

- The system handles three primary types of objects: `User`, `Subscription`, and `Service`.
- Data for these objects is stored in JSON or TXT files.
- The Abstract Factory design pattern is used to manage different file formats.
- The system processes data to generate detailed reports on user subscriptions.

# Project Title

**Description:** This project provides a system for managing services, subscriptions, and users, utilizing data processors to handle different file formats.

## Project Structure

Here's an overview of the project's directory structure:

      myproj/ 
         ├── file_repo/ 
            │ └── file_reader_factory.py 
         ├── model/ 
            ├── subscription.py 
            ├── user.py 
            ├── service.py
         ├── service.py/ 
            ├── subscription.py 
            ├── user.py 
            ├── service.py
app.py


- `file_repo/`: Contains classes for reading and processing data from files.
- `model/`: Contains data models like `Subscription`, `User`, and `Service`.
- `service/`: Contains repository classes and services for managing data.
- `app.py`: The main script for running the project.


### Installation

To set up the project locally using **Poetry**, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repository.git
   ```

2. Ensure you have Python 3.12 or higher installed.

3. Install **Poetry** if it's not already installed:
   ```bash
   pip install poetry
   ```

4. Install the project dependencies:
   ```bash
   poetry install
   ```

**Note:** Poetry will read the `pyproject.toml` file in the repository to install the required packages.

### Usage

To run the project and see how the system works, use the following command:

```bash
poetry run python app.py
```

### Adding Dependencies

If you need to add new packages, use:

```bash
poetry add package_name
```

The app.py script demonstrates how to use the data processors and repositories to manage services, subscriptions, and users.

## Example Usage

Here's a breakdown of what the app.py script does:

File Paths: Specifies file paths for data in different formats:

      SERVICE_JSON_FILENAME = 'data/data_service.json'
      SERVICE_CSV_FILENAME = 'data/data_service.csv'
      USER_JSON_FILENAME = 'data/data_user.json'
      USER_CSV_FILENAME = 'data/data_user.csv'
      SUBSCRIPTION_JSON_FILENAME = 'data/data_subscription.json'
      SUBSCRIPTION_CSV_FILENAME = 'data/data_subscription.csv

 
Create DataProcessors: Initializes data processors for different formats and sources:

      d1 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SERVICE)
      d2 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SERVICE)
      d3 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_USER)
      d4 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_USER)
      d5 = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SUBSCRIPTION)
      d6 = DataProcessor.create_processor(DataFormat.JSON, FactoryType.FROM_SUBSCRIPTION)

Process and Print Data: Demonstrates processing of data files and prints the results:

      s1 = ServiceRepo(d1.process(SERVICE_CSV_FILENAME))
      print(s1.get_services())

      s2 = ServiceRepo(d2.process(SERVICE_JSON_FILENAME))
      print(s2.get_services())

      ss1 = SubscriptionRepo(d5.process(SUBSCRIPTION_CSV_FILENAME))
      print(ss1.get_subscriptions())

      ss2 = SubscriptionRepo(d6.process(SUBSCRIPTION_JSON_FILENAME))
      print(ss2.get_subscriptions())

      u1 = UserRepo(d3.process(USER_CSV_FILENAME))
      print(u1.get_all_users())

      u2 = UserRepo(d4.process(USER_JSON_FILENAME))
      print(u2.get_all_users())

      print(ss1.get_subscriptions_by_user_id(1))
      print(ss1.get_subscriptions_by_service_id(2))

UserService Operations: Shows how to create a UserService and perform operations:

      user_service = UserService(u1, s1, ss1)
      print(user_service.active_subscriptions_report())

Data Processing

The DataProcessor class handles different data formats:

      TextData: Reads data from CSV files.
      JsonData: Reads data from JSON files.

Example:

      processor = DataProcessor.create_processor(DataFormat.TEXT, FactoryType.FROM_SERVICE)
      data = processor.process('data/data_service.csv')

Repository Classes

      ServiceRepo: Manages services with methods to retrieve, update, and delete services.
      SubscriptionRepo: Manages subscriptions with methods for adding, retrieving, and filtering subscriptions.
      UserRepo: Manages users with methods to retrieve, delete, and filter users.

User Service

The UserService class provides functionalities related to user subscriptions:

      subscriptions_for_user_id(user_id: int): Retrieves subscriptions for a given user ID.
      users_subscribed_to_service(service_id: int): Lists users subscribed to a given service ID.
      subscribe_user_to_service(user_id: int, service_id: int, quantity_per_month: int, discount: Decimal = None): Subscribes a user to a service.
      active_subscriptions_report(): Generates a report of active subscriptions.

Data Models

      Service: Represents a service with attributes like id_, name, category, and price.
      Subscription: Represents a subscription with attributes like user_id, service_id, quantity_per_month, discount, id_, and active.
      User: Represents a user with attributes such as name, surname, origin (from Destination enum), birthdate, and id_.
      Destination: Enum representing different destinations within Spain.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, please contact:

      Email: paulinapiotrowskap@gmail.com