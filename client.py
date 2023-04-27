# Import necessary modules
import requests
import json

# Set the base URL of the REST API
api_url = 'http://127.0.0.1:5000/'

# Start the main loop of the program
while True:
    # Display the menu options
    print("\n1. Get all user data")
    print("2. Get single user data")
    print("3. Create a new user")
    print("4. Update user data")
    print("5. Delete user data")
    print("6. Exit\n")

    # Prompt the user to select an option
    option = input("Select the option: ")

    if option == "1":
        # If the user selects option 1, send a GET request to the REST API to retrieve all user data
        try:
            response = requests.get(api_url + "user")
            # Convert the response data from JSON format to a Python dictionary
            all_users = response.json()
            # Print the data and the HTTP status code of the response to the console
            print(f'\n{all_users}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            # If an error occurs, print the error message to the console
            print(e)

    elif option == "2":
        # If the user selects option 2, prompt them to enter a user ID and send a GET request to the REST API to retrieve that user's data
        try:
            user_id = input("\nEnter user id: ")
            response = requests.get(api_url + "user/" + user_id)
            user = response.json()
            # If the HTTP status code of the response is 404 (Not Found), print an error message to the console
            if response.status_code == 404:
                print(response.text)
            else:
                # Otherwise, print the data for the requested user and the HTTP status code of the response to the console
                print(f'\n{user}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            # If an error occurs, print the error message to the console
            print(e)

    elif option == "3":
        # If the user selects option 3, prompt them to enter data for a new user and send a POST request to the REST API to create that user
        user_id = input("\nEnter user id: ")
        username = input("Enter username: ")
        number = input("Enter number: ")
        email = input("Enter email: ")
        new_user = {
            "user_id": user_id,
            "username": username,
            "number": number,
            "email": email
        }
        try:
            response = requests.post(api_url + "user", json=new_user)
            # Print the response data and the HTTP status code of the response to the console
            print(f'\n{response.text}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            # If an error occurs, print the error message to the console
            print(e)

    elif option == "4":
        # If the user selects option 4, prompt them to enter a user ID and choose which data to update, then send a PUT request to the REST API to update that user's data
        user_id = input("\nEnter user id: ")
        print("\nSelect an option to update")
        print("1. Update number")
        print("2. Update email")
        print("3. Update both number & email")

        # Read the user's choice and create a dictionary with the updated data
        sub_option = input('\nSelect the option: ')
        if sub_option == "1":
            number = input("\nEnter new number: ")
            data = {"number": number}
        elif sub_option == "2":
            email = input("\nEnter new email: ")
            data = {"email": email}
        elif sub_option == "3":
            number = input("\nEnter new number: ")
            email = input("Enter new email: ")
            data = {"number": number, "email": email}
        else:
            print("Invalid option selected")
            continue
        
        # Send a PUT request to update the user's data and print the response
        try:
            response = requests.put(api_url + "user/" + user_id, json=data)
            print(response.text)
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            print(e)


        
    # Delete user data
    elif option == "5":
        # Prompt the user for the user ID to delete and send a DELETE request to the API
        user_id = input("\nEnter user id to delete: ")
        try:
            response = requests.delete(api_url + "user/" + user_id)
            print(response.text)
            print(f"Status code: {response.status_code}")
        except Exception as e:
            print(e)

    # Exit program
    elif option == "6":
        print("\nExiting program...\n")
        break

    # Invalid option selected
    else:
        print("Invalid option selected")