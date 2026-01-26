import csv

class Contact:
    def __init__(self, name, phone):
        
        if phone.isdigit:()
            
        else :
            raise ValueError("phone number can only digit .")

        self.name = name
        self.phone = phone
        
class PhoneBook:
    def __init__(self):
        
        self.contacts = []

    def add_contact(self, name, phone):
        
        new_c = Contact(name, phone)
        self.contacts.append(new_c)

    def save_to_csv(self, filename = "new_contact.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            
            writer = csv.writer(f)
            writer.writerow(["name", "phone"])

            for c in self.contacts:
                writer.writerow([c.name, c.phone])

    def load_from_csv(self, filename = "new_contact.csv"):
        self.contacts = []

        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                
                for row in reader:
                    try:
                        self.add_contact(row[0], row[1])

                    except ValueError:
                        continue
                    
        except FileNotFoundError:
            pass
        
    def remove_contact(self, index) :
        
        if 0 <= index < len(self.contacts) :
            del self.contacts[index]

        else:
            raise IndexError("andis is wrong")

    def search_contacts(self, query):

        results = []

        for contact in self.contacts:
            
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results