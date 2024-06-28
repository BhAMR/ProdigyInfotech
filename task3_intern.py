# # -*- coding: utf-8 -*-
# """
# Created on Sun Jun 23 20:35:59 2024

# @author: HP
# """

# import json

# CONTACTS_FILE = 'contacts.json';

# def load_contacts():
#     try:
#         with open(CONTACTS_FILE,'r') as file:
#             return json.load(file)
#     except FileNotFoundError():
#             return []
        
# def save_contacts(contacts):
#     with open(CONTACTS_FILE,'w') as file:
#         json.dump(contacts,file,indent=4)
        
# def display_menu():
#     print("contact management system")
#     print("1.Add contact.")
#     print("2.View contact.")
#     print("3.Edit contact.")
#     print("4.Delete contact.")
#     print("5.Exit")
    
# def add_contact(contact):
#     name = input("enter name :")
#     phone = input("enter phone :")
#     email = input("enter email :")
#     contacts.append({"name":name, "phone":phone,"email":email})
#     save_contacts(contacts)
#     print("contact added successfully..")
    
# def view_contacts(contacts):
#     if not contacts:
#         print("no contact found..")
        
#     else:
#         for i,contact in enumerate(contacts,start=1):
#             print("{i}.{contact['name']} - {contact['phone']} - {contact['email']}")
            
# def edit_contact(contacts):
#     view_contacts(contacts)
#     if not contacts:
#         return
    
#     try:
#         contacts_index = int(input("enter number of contact to edit:")) -1
        
#         if 0 <= contacts_index < len(contacts):
#             contact = contacts[contacts_index]
#             contact['name'] = input("enter new name({contact['name']}):") or contact['name']
#             contact['phone'] = input("enter new phone({contact['phone']}):") or contact['phone']
#             contact['email'] = input("enter new email({contact['email']}):") or contact['email']
            
#             save_contacts(contacts)
#             print("contact updeted successfully..") 
            
#         else:
#           print("invalid contact number..")
          
#     except ValueError:
#         print("Invalid input..")
        
# def delete_contact(contacts):
#     view_contacts(contacts)
#     if not contacts:
#         return
    
#     try:
#         contact_index = int(input("Enter the number of the contact to delete: ")) - 1
#         if 0 <= contact_index < len(contacts):
#             contacts.pop(contact_index)
#             save_contacts(contacts)
#             print("Contact deleted successfully!")
#         else:
#             print("Invalid contact number.")
#     except ValueError:
#         print("Invalid input.")
            

# def main():
#     contacts = load_contacts()
    
#     while True:
#         display_menu()
#         choice = input("enter your choice :")
        
#         if choice == '1':
#             add_contact(contacts)
            
#         elif choice == '2':
#             view_contacts(contacts)
            
#         elif choice == '3':
#             edit_contact(contacts)
            
#         elif choice == '4':
#             delete_contact(contacts)
            
#         elif choice == '5':
#             print("Existing the program.")
#             break
#         else:
#             print("enter valid choice! please try again..")
            
# if __name__ == "__main__":
#     main()
        
                

import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email address ({contact['email']}): ") or contact['email']
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            contacts.pop(contact_index)
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
