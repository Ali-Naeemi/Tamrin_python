import csv
import os

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        if not phone_number.isdigit():
            raise ValueError("Shomare telephone bayad faghat [adad] bashad .\n")
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name}: {self.phone_number}"

class PhoneBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone):
        try:
            contact = Contact(name, phone)
            self.contacts.append(contact)
            print(f"Mokhatab '{name}' save shod.\n")
        except ValueError as e:
            raise ValueError(f"Format shomare eshtebah ast: {e}")
    
    def show_all(self):
        if not self.contacts:
            print("Dafterche telephone khali ast .\n")
            return
        print("List mokhatabin : \n")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")
        print()
    
    def save_to_csv(self, filename="Contacts.csv"):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Phone"])
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone_number])
            print(f"Mokhatab dar file '{filename}' save shod.")
        except PermissionError:
            print("Emkane neveshtan dar file vojod nadarad (shayad file baz ast).\n")
        except Exception as e:
            print(f"Khataye nashenakhte dar save kardan: {e}")
    
    def load_from_csv(self, filename="Contacts.csv"):
        if not os.path.exists(filename):
            print("\nFile mokhatabin peida nashod. Daftere jadid igad mishavad.\n")
            return
        
        loaded_contacts = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                
                for row_num, row in enumerate(reader, 1):
                    try:
                        if len(row) < 2:
                            continue
                        name, phone = row[0], row[1]
                        if not phone.isdigit():
                            raise ValueError
                        contact = Contact(name, phone)
                        loaded_contacts.append(contact)
                    except ValueError:
                        print(f"Dade namotabar dar satr {row_num} ignore shod.\n")
                    except Exception as e:
                        print(f"Khata dar pardazesh satr {row_num}: {e}")
            
            self.contacts = loaded_contacts
            print(f"\nEtelaat az file '{filename}' load shod.\n")
        except FileNotFoundError:
            print("File mokhatabin peida nashod.\n")
        except Exception as e:
            print(f"Khata dar reed file: {e}")

def main():
    phonebook = PhoneBook()
    phonebook.load_from_csv()
    
    while True:
        print("\nSystem modiriyat mokhatabin")
        print("=" * 30)
        print("1. Afzoodan mokhatab")
        print("2. Namayesh all mokhatabin")
        print("3. Save & khorooj")
        print("=" * 30)
        
        try:
            choice = int(input("Lotfan gozine mored nazar ra vared konid: "))
        except ValueError:
            print("Lotfan adad vared konid.\n")
            continue
        
        if choice == 1:
            name = input("Name mokhatab: ").strip()
            phone = input("Shomare telephone: ").strip()
            try:
                phonebook.add_contact(name, phone)
            except ValueError as e:
                print(f"{e} Try again.")
        
        elif choice == 2:
            phonebook.show_all()
        
        elif choice == 3:
            phonebook.save_to_csv()
            print("Exiting...")
            break
        
        else:
            print("Gozine namotabar. Lotfan adad [1,2,3] vared konid.")

if __name__ == "__main__":
    main()