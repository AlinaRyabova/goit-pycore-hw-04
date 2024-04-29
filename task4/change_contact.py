def change_contact(name, new_phone, contacts):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
