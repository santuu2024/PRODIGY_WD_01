import json
import os

FILENAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)
    choice = int(input("\nEnter contact number to edit: ")) - 1

    if 0 <= choice < len(contacts):
        contacts[choice]["name"] = input("New name: ")
        contacts[choice]["phone"] = input("New phone: ")
        contacts[choice]["email"] = input("New email: ")
        save_contacts(contacts)
        print("✏️ Contact updated!")
    else:
        print("❌ Invalid choice")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    choice = int(input("\nEnter contact number to delete: ")) - 1

    if 0 <= choice < len(contacts):
        contacts.pop(choice)
        save_contacts(contacts)
        print("🗑️ Contact deleted!")
    else:
        print("❌ Invalid choice")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n📒 Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
