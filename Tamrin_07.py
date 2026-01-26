# #Tamrin_07_01

# import csv

# class Contact:
    
#     def __init__(self, name, phone_number):
#         self.name = name
        
#         if phone_number.isdigit():
#             self.phone_number = phone_number
#         else:
#             raise ValueError("Phone number can digits only.")


# class PhoneBook:
    
#     def __init__(self):
#         self.contacts = []
    
#     def add_contact(self, name, phone):
#         new_contact = Contact(name, phone)
#         self.contacts.append(new_contact)
#         print(f"contact {name} added")
    
#     def save_to_csv(self):
#         try:
#             with open("Contact.csv", "w", newline="", encoding="UTF-8") as file:
#                 writer = csv.writer(file)
#                 writer.writerow(["Name", "Phone Number"])
#                 for c in self.contacts:
#                     writer.writerow([c.name, c.phone_number])
#                 print("saved ...")
#         except PermissionError:
#             print("Unable to write to file.")
    
#     def load_from_csv(self):
#         try:
#             with open("Contact.csv", "r", encoding="UTF-8") as file:
#                 reader = csv.reader(file)
#                 next(reader)
#                 for row in reader:
#                     if len(row) >= 2:
#                         name = row[0]
#                         phone = row[1]
#                         try:
#                             self.add_contact(name, phone)
#                         except ValueError:
#                             print(f"Invalid phone number for {name}: {phone}")
#         except FileNotFoundError:
#             self.contacts = []


# phonebook = PhoneBook()

# while True:
#     print("\nPhoneBock Menu :")
#     print("1. Add Contact")
#     print("2. All Contact")
#     print("3. Save & Exit")
    
#     choice = input("Enter your choice (1-3): ")
    
#     if choice == "1":
#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")
#         try:
#             phonebook.add_contact(name, phone)
#         except ValueError:
#             print("The number format is wrong. try again.")
    
#     elif choice == "2":
#         print("\nAll Contacts :")
#         if not phonebook.contacts:
#             print("No contacts available.")
#         else:
#             for i in range(len(phonebook.contacts)):
#                 contact = phonebook.contacts[i]
#                 print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone_number}")
    
#     elif choice == "3":
#         phonebook.save_to_csv()
#         print("Saved . Exiting ...")
#         break
    
#     else:
#         print("Wrong choice. please enter 1 or 2 or 3.")
        
#################################################

#Tamrin_07_02

# import csv

# class Contact:
    
#     def __init__(self, name, phone_number):
#         self.name = name
        
#         if phone_number.isdigit():
#             self.phone_number = phone_number
#         else:
#             raise ValueError("Phone number can digits only.")


# class PhoneBook:
    
#     def __init__(self):
#         self.contacts = []
    
#     def add_contact(self, name, phone):
#         new_contact = Contact(name, phone)
#         self.contacts.append(new_contact)
#         print(f"contact {name} added")
    
#     def save_to_csv(self):
#         try:
#             with open("Contact.csv", "w", newline="", encoding="UTF-8") as file:
#                 writer = csv.writer(file)
#                 writer.writerow(["Name", "Phone Number"])
#                 for c in self.contacts:
#                     writer.writerow([c.name, c.phone_number])
#                 print("saved ...")
#         except PermissionError:
#             print("Unable to write to file.")
    
#     def load_from_csv(self):
#         try:
#             with open("Contact.csv", "r", encoding="UTF-8") as file:
#                 reader = csv.reader(file)
#                 next(reader)
#                 for row in reader:
#                     if len(row) >= 2:
#                         name = row[0]
#                         phone = row[1]
#                         try:
#                             self.add_contact(name, phone)
#                         except ValueError:
#                             print(f"Invalid phone number for {name}: {phone}")
#         except FileNotFoundError:
#             self.contacts = []


# def main():
#     phonebook = PhoneBook()
    
#     while True:
#         print("\nPhoneBock Menu :")
#         print("1. Add Contact")
#         print("2. All Contact")
#         print("3. Save & Exit")
        
#         choice = input("Enter your choice (1-3): ")
        
#         if choice == "1":
#             name = input("Enter name: ")
#             phone = input("Enter phone number: ")
#             try:
#                 phonebook.add_contact(name, phone)
#             except ValueError:
#                 print("The number format is wrong. try again.")
        
#         elif choice == "2":
#             print("\nAll Contacts :")
#             if not phonebook.contacts:
#                 print("No contacts available.")
#             else:
#                 for i in range(len(phonebook.contacts)):
#                     contact = phonebook.contacts[i]
#                     print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone_number}")
        
#         elif choice == "3":
#             phonebook.save_to_csv()
#             print("Saved . Exiting ...")
#             break
        
#         else:
#             print("Wrong choice. please enter 1 or 2 or 3.")


# if __name__ == "__main__":
#     main()

######################################################

#Tamrin_07_03

import csv
import os

class Contact:
    
    def __init__(self, name, phone_number):
        self.name = name
        
        if phone_number.isdigit():
            self.phone_number = phone_number
        else:
            raise ValueError("Phone number can digits only.")


class PhoneBook:
    
    def __init__(self):
        self.contacts = []
        self.load_from_csv()
    
    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)
        print(f"contact {name} added")
    
    def save_to_csv(self):
        try:
            with open("Contact.csv", "w", newline="", encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone Number"])
                for c in self.contacts:
                    writer.writerow([c.name, c.phone_number])
                print("saved ...")
        except PermissionError:
            print("Unable to write to file.")
    
    def load_from_csv(self):
        try:
            if not os.path.exists("Contact.csv"):
                print("No existing contacts file found.")
                return
            
            with open("Contact.csv", "r", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) >= 2:
                        name = row[0]
                        phone = row[1]
                        try:
                            new_contact = Contact(name, phone)
                            self.contacts.append(new_contact)
                        except ValueError:
                            print(f"Invalid phone number for {name}: {phone}")
                print(f"Loaded {len(self.contacts)} contacts from file.")
        except FileNotFoundError:
            print("Contacts file not found.")
            self.contacts = []
        except Exception as e:
            print(f"Error loading contacts: {e}")
            self.contacts = []


def main():
    phonebook = PhoneBook()
    
    while True:
        print("\nPhoneBock Menu :")
        print("1. Add Contact")
        print("2. All Contact")
        print("3. Save & Exit")
        print("4. Reload from file")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            try:
                phonebook.add_contact(name, phone)
            except ValueError:
                print("The number format is wrong. try again.")
        
        elif choice == "2":
            print("\nAll Contacts :")
            if not phonebook.contacts:
                print("No contacts available.")
            else:
                for i, contact in enumerate(phonebook.contacts, 1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        
        elif choice == "3":
            phonebook.save_to_csv()
            print("Saved . Exiting ...")
            break
        
        elif choice == "4":
            print("Reloading contacts from file...")
            phonebook.contacts = []
            phonebook.load_from_csv()
        
        else:
            print("Wrong choice. please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
