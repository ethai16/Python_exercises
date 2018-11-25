phonebook = {
    "Erick": "713-123-1234"
}

usePhonebook = True

def query(): 
    print("Electronic Phone Book")
    print("=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

while usePhonebook == True:
    query()

    choice = str(input("What do you want to do? (1-5)"))

    if choice == "1":
        pickName = str(input("Name: "))
        getName = phonebook.get(pickName)
        print(f"Found entry for {pickName} : ", getName )

    elif choice == "2":
        addName = str(input("Name: "))
        addNumber = str(input("Phone Number: "))
        phonebook[addName] = addNumber 
        print(f"Entry stored for {addName}")

    elif choice == "3":
        delName = str(input("Name: "))
        del phonebook[delName]
        print(f"Deleted entry for {delName}")

    elif choice ==  "4":
        for key, value in phonebook.items():
            print(f"Found entry for {key}: {value}")

    else:
        print("Goodbye")
        usePhonebook = False
        