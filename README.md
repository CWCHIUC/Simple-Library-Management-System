# Simple-Library-Management-System
Library Management System School Project
Welcome to the Library Management System! This Python application allows you to manage a library's collection of books and DVDs. You can browse books, check availability, print ratings, check in/out items, and even open books for reading.

## Getting Started
Prerequisites
Before you begin, make sure you have Python installed on your system. You can download Python from the official website: python.org.

## Installation
Clone or download the repository to your local machine.

git clone https://github.com/CWCHIUC/Simple-Library-Management-System.git
Navigate to the project directory.

cd library-management-system
Make sure you have the required JSON database files in the project directory:

books.json: Contains information about books.
dvd.json: Contains information about DVDs.
You can modify these JSON files to add or update items in the library.

## Usage
Open a terminal and navigate to the project directory.

Run the main.py script to start the Library Management System:

python main.py
You will be prompted to generate a library card. Enter any card number you like.

Enter your library access card number when prompted.

You can now use the following actions in the Library Management System:

- Browse Books (1): View the available books in the library. 
- Check Availability of a Book (2): Check if a specific book is available.
- Print Rating of a Book (3): Print the rating of a book.
- Check Out a Book (4): Borrow a book from the library.
- Check In a Book (5): Return a borrowed book to the library.
- Open a Book (6): Read a book that you have borrowed.
- Exit (7): Quit the Library Management System.

Follow the on-screen prompts to perform your desired actions.

## JSON Database Files
books.json: This file contains information about books in the library. You can modify it to add, remove, or update book entries. Each book has an item ID, status (available or checked out), and a rating.

dvd.json: This file contains information about DVDs in the library. You can similarly modify it to manage DVD entries.

## Additional Information
Valid Input: When entering the name of a book or DVD, make sure to use the exact name as it appears in the database. The system will check for validity.

Due Dates: Books that are checked out will have a default due date of "7 days."

Status: Books can be "available" or "checked out" based on their status.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thank you for using the Library Management System. If you encounter any issues or have suggestions for improvements, please feel free to contribute to the project.

Feel free to customize the README further based on your specific needs or additional information about the project.
