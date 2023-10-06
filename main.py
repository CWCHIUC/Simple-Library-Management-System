from book import Book, valid_input
from library import Library

def main():
    print("Welcome to the Library Management System!")

    # Generate a library card for the user
    library_card = Library().generate_card()
    print(f"Your Library Card Number: {library_card}")

    # Ask for user input to enter the library
    input_card = input("Enter your library access card number: ")

    if input_card != library_card:
        print("Access Denied. Invalid library access card number.")
        return

    while True:
        print("\nActions:")
        print("1. Browse Books")
        print("2. Check Availability of a Book")
        print("3. Print Rating of a Book")
        print("4. Check Out a Book")
        print("5. Check In a Book")
        print("6. Open a Book")
        print("7. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            # Browse available books
            print("Available Books:")
            Book().browse_book()
            print()

        elif choice == "2":
            # Check availability of a book
            book_name = input("Enter the name of the book: ")
            if valid_input(book_name):
                Book().check_availability(book_name)
            else:
                print("Book not found.")
            print()

        elif choice == "3":
            # Print rating of a book
            book_name = input("Enter the name of the book: ")
            if valid_input(book_name):
                Book().print_rating(book_name)
            else:
                print("Book not found.")
            print()

        elif choice == "4":
            # Check out a book
            book_name = input("Enter the name of the book to check out: ")
            if valid_input(book_name):
                Book().check_out(book_name)
                Book().update_status(book_name)
            else:
                print("Book not found.")
            print()

        elif choice == "5":
            # Check in a book
            book_name = input("Enter the name of the book to check in: ")
            if valid_input(book_name):
                Book().check_in(book_name)
                Book().update_status(book_name)
                Book().remove_due(book_name)
            else:
                print("Book not found.")
            print()

        elif choice == "6":
            # Open a book
            book_name = input("Enter the name of the book to open: ")
            if valid_input(book_name):
                Book().open_book(book_name)
            else:
                print("Book not found.")
            print()

        elif choice == "7":
            print()
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print()
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()