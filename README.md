# user-rest-api-client

This is a simple Python program that demonstrates how to create a RESTful API with Flask for managing user data. 

## Installation

1.Clone the repository

2. Install the required dependencies by running:

```
pip install -r requirements.txt
```

3. Run the program with:

```
python client.py
```

## Usage

The program provides a simple command-line interface for interacting with the API. Here are the available options:

1. Get all user data
2. Get single user data
3. Create a new user
4. Update user data
5. Delete user data
6. Exit

To select an option, simply enter the corresponding number at the prompt. 

### Examples

## 1) Get all user data

```
Select the option: 1

Output:

[{'user_id': '1', 'username': 'John', 'number': '1234567890', 'email': 'john@example.com'}, {'user_id': '2', 'username': 'Mark', 'number': '0987654321', 'email': 'Mark@example.com'}]

Status code: 200
```

## 2) Get single user data

```
Select the option: 2

Input:

    Enter user id: 1

Output:

    {'user_id': '1', 'username': 'John', 'number': '1234567890', 'email': 'john@example.com'}

    Status code: 200
```

## 3) Create a new user

```
Select the option: 3

Input:
    Enter user id: 3
    Enter username: Alice
    Enter number: 5551234
    Enter email: alice@example.com

Output:

    {"message": "User created successfully"}

    Status code: 201
```

## 4) Update user data

```
Select the option: 4

Input:

    Enter user id: 1

    Select an option to update
    1. Update number
    2. Update email
    3. Update both number & email

    Select the option: 2

    Enter new email: johndoe@gmail.com

Output:

    {"message": "User updated successfully"}

    Status code: 200
```

## 5) Delete user data

```
Select the option: 5

Input:

    Enter user id to delete: 2

Output:

    {"message": "User deleted successfully"}

    Status code: 200
```

## 6) Exit

    This while exit the program.....