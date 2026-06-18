contacts = []


# ---------------- Validation ----------------

import re

def valid_phone(phone):
    phone = phone.replace(" ", "")

    pattern = r"^(?:\+256|256|0)(7[0-9])[0-9]{7}$"
    return bool(re.match(pattern, phone))


def format_phone(phone):
    phone = phone.replace(" ", "")

    if phone.startswith("0") and len(phone) == 10:
        return "+256" + phone[1:]

    if phone.startswith("256") and len(phone) == 12:
        return "+" + phone

    if phone.startswith("+256"):
        return phone

    return phone


def valid_email(email):
    return email == "" or ("@" in email and "." in email)


# ---------------- Display Helper ----------------

def show(results):
    if not results:
        print("No contacts found")
        return

    print("\n--- Contacts ---")
    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


# ---------------- CRUD ----------------

def add():
    name = input("Name: ")
    phone = input("Phone: ")

    if not valid_phone(phone):
        print("Invalid Ugandan number")
        return

    phone = format_phone(phone)

    email = input("Email: ")

    if not valid_email(email):
        print("Invalid email")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    print("Contact added")


def view():
    name = input("Name: ").lower()

    for c in contacts:
        if c["name"].lower() == name:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}")
            return

    print("Not found")


def update():
    name = input("Name: ").lower()

    for c in contacts:
        if c["name"].lower() == name:

            phone = input("New phone: ")

            if not valid_phone(phone):
                print("Invalid phone")
                return

            c["phone"] = format_phone(phone)

            email = input("New email: ")

            if not valid_email(email):
                print("Invalid email")
                return

            c["email"] = email

            print("Updated")
            return

    print("Not found")


def delete():
    name = input("Name: ").lower()

    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Deleted")
            return

    print("Not found")


# ---------------- Search ----------------

def search():
    key = input("Search: ").lower()

    results = [
        c for c in contacts
        if key in c["name"].lower()
        or key in c["phone"]
        or key in c["email"].lower()
    ]

    show(results)


def list_all():
    show(contacts)


# ---------------- Menu ----------------

def main():
    while True:
        print("\nContact Manager")
        print("1.Add 2.View 3.Update 4.Delete 5.Search 6.List 7.Exit")

        choice = input("Choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            search()
        elif choice == "6":
            list_all()
        elif choice == "7":
            print("Bye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()




    
    
   

   


        