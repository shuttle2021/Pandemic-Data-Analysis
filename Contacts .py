
database = {"shuttle":9080590855,"barath":638383877,"hannah":6987237898}

print("\nGreeting\'s from Vigneshwaram")

print("Welcome to phoneBook\n")


while True:
    print("Type EDIT to edit the contact number\n     CREATE to create a new contact\n     SEARCH to search a specific contact\n     DELETE to Delete the contact\n     VIEW to view all contacts in PhoneBook")
    
    print('')
    function = input("Enter the function: ").lower()


    def view():
        print('')
        print("Here is your phoneBook :- ")
        print(database)
        print('')
        
    def create():
        print('')
        name = input("Enter the name of the contact: ")
        number = int(input("Enter the number of the contact: "))
        print('')
        database.setdefault(name,number)
        print("Contact updated succesfully")
        print('')
        print(database)
        
        print('')

    def delete():
        print('')
        print(database)
        print('')
        delete = input("Enter contact to delete: ")
        print('')
        
        if delete in database:
            database.pop(delete)
            print(database)
            print('')
            print("Contact succesfully deleted !!")
            print('')
            
        else:
            print("Given contact doesn\'t exist in phoneBook !!")
            print('')
        
    def search():
        print('')
        search = input("Enter contact to search: ")
        print('')
        if search in database:
            print(database[search])
            print('')
            
        if search not in database:
            print('')
            print("Contact doesn't exist in Phonebook !!")
            print('')
            print("Do you want to create that contact?")
            print('')
            function1 = input("CREATE to create or EXIT to ignore: ").lower()
            if function1 == "create":
                print('')
                create()
            elif function1 == "exit":
                print('')
                pass
            else:
                print('')
                print("Invalid input from user contact admin(Vignesh)")
                print('')

    def edit():
        print('')
        print(database)
        print('')
        
        edit = input("Enter the contact which you want to edit: ")
        print('')
        
        if edit in database:
            
            editNumber = int(input("Enter the new number: "))
            database[edit] = editNumber
            print('')
            print("Contact updated succesfully")
            print('')
            print(database)
            print('')
            
        else:
            
            print("Given contact doesn't exist in Phonebook")
            print('')
            sys.exit()

    if function == "edit":
        edit()
    elif function == "create":
        create()
    elif function == "search":
        search()
    elif function == "delete":
        delete()
    elif function == "view":
        view()
    else:
        print('')
        print("Invalid user input contact admin(Vignesh)\n")


    responce = input("Type \'RUN\' to keep your phoneBook open or \'EXIT\' to close your phoneBook: ").lower()
    print('')
    if responce == 'run':
        print('')
        print("Welcome back!!")
        continue
    elif responce == 'exit':
        print('')
        print('Hope you had a nice time !!')
        break
    else:
        print('')
        print(' Program has been discontinued due to Invalid input from user\n To continue run the file or contact Vignesh ')
        print('')
        break


    
