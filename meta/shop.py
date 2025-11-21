import json
import os
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_info_contact(self):
        return f"""
    Name:{self.name}
    Phone Number:{self.phone_number}
    Email:{self.email}
    """
    def to_dict(self):
        return {
            "name":self.name,
            "phone_number":self.phone_number,
            "email":self.email
        }
class Smsmanager:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def take_sms(self,receiver_phone):
        try:
            with open("contacts.json", "r") as contacts:
                data = json.load(contacts)
                if receiver_phone in data:
                    print(f"sms {receiver_phone}ga yuborildi")
        except (FileNotFoundError, json.JSONDecoder) as r:
            print(f"Xato {r}")
class Phone:
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        self.contacts = []

    def load_json(self):
        if os.path.exists(self.filename):
            with open(os.path.join(self.filename), "r") as f:
                data = json.load(f)
                for item in data:
                    main = Contact(item["name"], item["phone_number"], item["email"])
                    self.contacts.append(main)

    def save_json(self):
        data = [key.to_dict() for key in self.contacts]
        with open(self.filename, "w") as name:
            json.dump(data, name, indent=4)

    def add_contact(self, new_contact):
        if new_contact not in self.contacts:
            self.contacts.append(new_contact)
            self.save_json()

    def update_contact(self, old_name, new_name = None, new_phone_number = None, new_email = None,):
        for item in self.contacts:
            if item.name == old_name:
                if new_name:
                    item.name = new_name
                if new_phone_number:
                    item.phone_number = new_phone_number
                if new_email:
                    item.email = new_email
                self.save_json()
                return True
            return False
    def remove_contact(self, deleted_contact):
        b = [x for x in self.contacts if x == deleted_contact]
        if len(b) > 0:
            self.contacts.remove(deleted_contact)
            self.save_json()
        else:
            print("xato")
    def view_contacts(self):
        for item in self.contacts:
            print(item.to_dict())
s1 = Phone("Iphone", "contacts.json")

def menu():
    print("\nPhone Book Options:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Remove Contact")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            # View all contacts
            s1.view_contacts()

        elif choice == '2':
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            new_contact = Contact(name, phone_number, email)
            s1.add_contact(new_contact)
            print(f"Contact {name} added.")

        elif choice == '3':
            old_name = input("Enter the name of the contact you want to update: ").strip()
            new_name = input("Enter new name (or press Enter to skip): ").strip() or None
            new_phone_number = input("Enter new phone number (or press Enter to skip): ").strip() or None
            new_email = input("Enter new email (or press Enter to skip): ").strip() or None
            if s1.update_contact(old_name, new_name, new_phone_number, new_email):
                print(f"Contact {old_name} updated.")
            else:
                print(f"Contact {old_name} not found.")

        elif choice == '4':
            name_to_remove = input("Enter the name of the contact you want to remove: ").strip()
            contact_to_remove = None
            for contact in s1.contacts:
                if contact.name == name_to_remove:
                    contact_to_remove = contact
                    break
            if contact_to_remove:
                s1.remove_contact(contact_to_remove)
                print(f"Contact {name_to_remove} removed.")
            else:
                print(f"Contact {name_to_remove} not found.")

        elif choice == '5':
            print("Exiting phone book...")
            break
        else:
            print("Invalid option. Please choose between 1-5.")
main()