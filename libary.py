import json

# Load data
try:
    with open("lib.json", "r") as file:
        lib = json.load(file)
except FileNotFoundError:
    lib = {}

def addbook():
    book = input("Enter the book name: ")

    if book == "":
        print("Book name can't be empty")
        return
    
    author = input("Enter the name of the author :")

    if author =="":
        print("Author can't be empty")
        return
    
    if book in lib:
        print("Book already Exist")
        return
    
    

    print("Book Name:", lib[book]["book name"])
    print("Author Name:", lib[book]["author name"])

    print("Book added successfully!")

def viewbook():
    book = input("Enter the name of the book: ")

    if book == "":
        print("Book name can't be empty")
        return

    if book in lib:
        print("\nBook Found")
        print("Book Name:", lib[book]["book name"])
    else:
        print("Book not found.")

def view_all_book():
    if not lib:
        print("No Book in LIBARY")
        return
    print("ALL BOOKS ARE:")

    for book in lib:
        print("Book Name =", lib[book]["book name"])
        print("Author =", lib[book]["author name"])

def delete_book():
    delete_book = input("Enter the name of the book :")
    if delete_book == "": 
        print("DELETE CAN'T BE EMPTY")
        return
    if delete_book in lib:
        confirm = input("Are you sure you wanna delete it(yes/no)")
        if confirm.lower() == "yes":

    
        
            lib.pop(delete_book)
            print("Deleted successfully")

        with open("lib.json", "w") as file:
            json.dump(lib, file, indent=4)
    
    else:
        print("Book not found")

        
        

while True:
    print("\n === LIBRARY === ")
    print("1. Add Book")
    print("2. View Book")
    print("3. View All Books")
    print("4. Delete books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addbook()

    elif choice == "2":
        viewbook()

    elif choice == "3":
        view_all_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        with open("lib.json", "w") as file:
            json.dump(lib, file, indent=4)

        print("Total Books =", len(lib))
        print("Exiting...")
        break

    else:
        print("Invalid choice!")