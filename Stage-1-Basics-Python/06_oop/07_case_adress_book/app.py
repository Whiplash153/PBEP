class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def show_all(self):
        if not self.contacts:
            print("Address book is empty")
        else:
            for contact in self.contacts:
                print(contact)

if __name__ == "__main__":
    book = AddressBook()

    book.add_contact(Contact("Anna", "12345"))
    book.add_contact(Contact("Bob", "67890"))
    book.add_contact(Contact("Kate", "54321"))

    result = book.find_contact("Bob")
    if result:
        print("Found:", result)
    else:
        print("Not found")

    print("\nAll contacts")
    book.show_all()