import os
import pickle

# Function to read contacts from a text file
def read_contacts_from_text(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, 'r') as file:
        contacts = [line.strip() for line in file.readlines()]
    return contacts

# Function to write contacts to a text file
def write_contacts_to_text(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

# Function to add a contact
def add_contact_to_text(file_name, contact):
    contacts = read_contacts_from_text(file_name)
    contacts.append(contact)
    write_contacts_to_text(file_name, contacts)

# Function to remove a contact
def remove_contact_from_text(file_name, contact):
    contacts = read_contacts_from_text(file_name)
    if contact in contacts:
        contacts.remove(contact)
        write_contacts_to_text(file_name, contacts)
    else:
        print("Contact not found.")

# Function to display all contacts
def display_contacts_from_text(file_name):
    contacts = read_contacts_from_text(file_name)
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

# Function to read contacts from a binary file
def read_contacts_from_binary(file_name):
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, 'rb') as file:
            contacts = pickle.load(file)
    except (EOFError, pickle.UnpicklingError):
        print("Error reading the binary file. It might be corrupted.")
        return []
    return contacts

# Function to write contacts to a binary file
def write_contacts_to_binary(file_name, contacts):
    with open(file_name, 'wb') as file:
        pickle.dump(contacts, file)

# Function to add a contact
def add_contact_to_binary(file_name, contact):
    contacts = read_contacts_from_binary(file_name)
    contacts.append(contact)
    write_contacts_to_binary(file_name, contacts)

# Function to remove a contact
def remove_contact_from_binary(file_name, contact):
    contacts = read_contacts_from_binary(file_name)
    if contact in contacts:
        contacts.remove(contact)
        write_contacts_to_binary(file_name, contacts)
    else:
        print("Contact not found.")

# Function to display all contacts
def display_contacts_from_binary(file_name):
    contacts = read_contacts_from_binary(file_name)
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

# User interaction function
def user_interaction():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display Contacts")
    print("4. Exit")

    file_name_text = 'contacts.txt'
    file_name_binary = 'contacts.bin'

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            contact = input("Enter contact name: ")
            file_type = input("Save to text or binary file (text/binary)? ")
            if file_type == 'text':
                add_contact_to_text(file_name_text, contact)
            elif file_type == 'binary':
                add_contact_to_binary(file_name_binary, contact)
            else:
                print("Invalid file type selected.")
        elif choice == '2':
            contact = input("Enter contact name to remove: ")
            file_type = input("Remove from text or binary file (text/binary)? ")
            if file_type == 'text':
                remove_contact_from_text(file_name_text, contact)
            elif file_type == 'binary':
                remove_contact_from_binary(file_name_binary, contact)
            else:
                print("Invalid file type selected.")
        elif choice == '3':
            file_type = input("Display contacts from text or binary file (text/binary)? ")
            if file_type == 'text':
                display_contacts_from_text(file_name_text)
            elif file_type == 'binary':
                display_contacts_from_binary(file_name_binary)
            else:
                print("Invalid file type selected.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interaction()
