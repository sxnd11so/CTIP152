# User input is stored inside the dictionary a
Librarian_data = {}

# Lists to store all books
Books = []


# Sections A: Main menu screen
def menu_screen():
    # Loops until user selects shutdown
    while True:
        print("==============Digital Archive Portal========")
        print('1. Register librarian')
        print('2. Staff login')
        print('3. Shut downs')
        print('=========================')

        try:
            choice = int(input("Choose a number: "))

            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid menu option")
        except ValueError:
            print("Please enter a valid number")





# Validates staff id
def valid_staffID(staff_id):
    return len(staff_id) == 6 and "." in staff_id

# Validates password complexity
def valid_password(password):
    has_upper = False
    has_digit = False
    has_operator = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
        if ch in "+-*/":
            has_operator = True
    return len(password) >= 10 and has_upper and has_digit and has_operator

# Collects and checks librarian details
def register():
    first_name = input("Enter name: ")
    last_name = input("Enter surname: ")
    staff_id = input("Enter staff ID: ")
    password = input("Enter password: ")

    while not valid_staffID(staff_id):
        print("Invalid staff ID. Try again(id must contain a period")
        staff_id = input("Enter staff ID: ")


    while not valid_password(password):
        print("Invalid password. Try again")
        print("Password must have an upper case letter, digits and any of this operators(+, -,*,/ ")
        password = input("Enter valid password: ")



    Librarian_data[staff_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    }

    print("Registered successfully")

# verifies staff credentials
def login():

    attempts = 3

    while attempts > 0:

        user_id = input("Enter staff ID: ")
        user_password = input("Enter password: ")

        if user_id in Librarian_data:

            if Librarian_data[user_id]["password"] == user_password:
                print(f"Welcome {Librarian_data[user_id]['first_name']}")
                book_dashboard()

            else:
                attempts -= 1
                print(f"Incorrect password. Attempts left: {attempts}")

        else:
            attempts -= 1
            print(f"Staff ID not found. Attempts left: {attempts}")

    print("Account locked. Too many failed attempts.")

# creates a book dictionary and appends it to the book list
def add_book(title, author, code, accession_number):
    book = {"title": title, "author": author, "code": code, "accession number": accession_number}
    Books.append(book)

# Auto-generates a unique accession number for each book
def generate_accession_number(title, index):

    short_title = title.replace(" ", "")[:3].upper()

    return f"BK-{short_title}-{str(index).zfill(2)}"


# Returns the full list of books
def view_books():
    return Books
# Searches for the book by title
def search_book(title):
    return [book for book in Books if book['title'].lower() == title.lower()]

# Removes the book by title
def delete_books(title):
    global Books
    Books = [book for book in Books if book['title'].lower() != title.lower()]

def report():
    print("Coming Soon!")

# Section B: Inventory Dashboard menu
def book_dashboard():
    while True:
        print("\n---------Inventory Dashboard Menu------------")
        print("1. Add Books")
        print("2. View Books")
        print("3. Search Books")
        print("4. Delete Books")
        print("5. Generate Inventory Report")
        print("6. Logout")
        print("--------------------------------")

        try:
            menu_choice = int(input("Enter your choice (1-6): "))

            if menu_choice == 1:

                num_books = int(input("Enter number of books  to add: "))
                if num_books <= 0:
                    print("Invalid vaule. Try again!")
                    return

                for i in range(num_books):

                    title = input("Enter book title: ")

                    while len(title) > 30:
                        print("Title too long. Try again")
                        title = input("Enter book title: ")

                    author = input("Enter the author: ")

                    isbn = input("Enter the ISBN code: ")

                    while len(isbn) != 13 or not isbn.isdigit():
                        print("Invalid ISBN code. Try again")
                        isbn = input("Enter the ISBN code: ")

                    accession_number = generate_accession_number(
                        title,
                        len(Books) + 1
                    )

                    add_book(
                        title,
                        author,
                        isbn,
                        accession_number
                    )

                    print("Book has been added successfully.")

            elif menu_choice == 2:
                all_books = view_books()
                if not all_books:
                    print("No books found.")
                else:
                    for i, book in enumerate(all_books, start=1):
                        print(f"{i}. {book['title']} by {book['author']} ({book['accession number']})")
            elif menu_choice == 3:
                title = input("Enter title to seacrh: ")
                found = search_book(title)
                if found:
                    for book in found:
                        print(f"{book['title']} by {book['author']} ({book['accession number']})")
                else:
                    print("Books not found.")

            elif menu_choice == 4:
                title = input("Enter title to delete: ")
                delete_books(title)
                print(f"{title} has been deleted (if it existed). ")

            elif menu_choice == 5:
                report()

            elif menu_choice == 6:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again. ")

        except ValueError:
            print("Please enter a valid number")






if __name__ == "__main__":
    menu_screen()

