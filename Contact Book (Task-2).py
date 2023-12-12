contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully!")

def display_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for name, details in contacts.items():
            print(f"{name}: {details['phone']}")

def search_contact(keyword):
    results = []
    for name, details in contacts.items():
        if keyword.lower() in name.lower() or keyword in details['phone']:
            results.append((name, details)
    return results

def update_contact(name):
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: )
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} updated successfully!")
    
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()

        elif choice == '2':
            display_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = search_contact(keyword)
            if results:
                print("Search results:")
                for name, details in results:
                    print(f"{name}: {details['phone']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            update_contact(name)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
