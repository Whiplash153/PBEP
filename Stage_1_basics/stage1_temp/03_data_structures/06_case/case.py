Contact = dict

contacts: list[Contact] = []

names_index: set[str] = set()

def make_contact(name: str, phone: str) -> Contact:
    return {"name": name.strip(), "phone": phone.strip()}

def add_to_storage(contact: Contact) -> None:
    contacts.append(contact)
    names_index.add(contact["name"])

def add_contact():
    name = input("Enter name: ").strip()
    if name in names_index:
        print(f"Contact '{name}' already exists.")
        return

    phone = input("Enter phone: ").strip()
    contact = make_contact(name, phone)
    add_to_storage(contact)
    print(f"Added: {name} -> {phone}")

def show_all_contacts():
    if not contacts:
        print("No contacts")
        return
    print("\nContacts:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} -> {c['phone']}")

def find_contact():
    query = input("Search name: ").strip().lower()
    if not query:
        print("Empty query")
        return
    results = [c for c in contacts if query in c["name"].lower()]
    if not results:
        print("No matches")
        return
    print("\nFound:")
    for i, c in enumerate(results, start=1):
        print(f"{i}. {c['name']} -> {c['phone']}")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name not in names_index:
        print(f"No contact with name '{name}'")
        return

    global contacts
    contacts = [c for c in contacts if c["name"] != name]

    names_index.remove(name)

    print(f"Deleted contact '{name}'")

def show_stats():
    total_contacts = len(contacts)
    unique_names = len(names_index)

    print("\n--- Stats ---")
    print(f"Total contacts: {total_contacts}")
    print(f"Unique names: {unique_names}")

def main_menu():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Find contact by name")
        print("4. Delete contact")
        print("5. Show stats")
        print("0. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_stats()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Unknown option. Try again.")

if __name__ == "__main__":
    main_menu()
