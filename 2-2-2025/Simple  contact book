contacts = {}

while True:
    action = input("(add/show/search/delete/exit): ").strip().lower()
    
    if action == "add":
        contacts[input("Name: ")] = input("Number: ")
    elif action == "show":
        print("\n".join(f"{k}: {v}" for k, v in contacts.items()) or "No contacts.")
    elif action == "search":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))
    elif action == "delete":
        contacts.pop(input("Delete name: "), print("Not found"))
    elif action == "exit":
        break
