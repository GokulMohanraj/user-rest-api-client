import requests
import json

api_url = 'http://127.0.0.1:5000/'

while True:
    print("\n1. Get all user data")
    print("2. Get single user data")
    print("3. Create a new user")
    print("4. Update user data")
    print("5. Delete user data")
    print("6. Exit\n")

    option = input("Select the option: ")

    if option == "1":
        try:
            response = requests.get(api_url + "user")
            all_users = response.json()
            print(f'\n{all_users}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            print(e)

    elif option == "2":
        try:
            user_id = input("\nEnter user id: ")
            response = requests.get(api_url + "user/" + user_id)
            user = response.json()
            if response.status_code == 404:
                print(response.text)
            else:
                print(f'\n{user}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            print(e)

    elif option == "3":
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
            print(f'\n{response.text}')
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            print(e)

    elif option == "4":
        user_id = input("\nEnter user id: ")
        print("\nSelect an option to update")
        print("1. Update number")
        print("2. Update email")
        print("3. Update both number & email")

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

        try:
            response = requests.put(api_url + "user/" + user_id, json=data)
            print(response.text)
            print(f"\nStatus code: {response.status_code}")
        except Exception as e:
            print(e)

    elif option == "5":
        user_id = input("\nEnter user id to delete: ")
        try:
            response = requests.delete(api_url + "user/" + user_id)
            print(response.text)
            print(f"Status code: {response.status_code}")
        except Exception as e:
            print(e)

    elif option == "6":
        print("\nExiting program...\n")
        break

    else:
        print("Invalid option selected")
