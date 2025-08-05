from library import Library
from user import User, Admin
from book import Book

def main():
    library = Library()

    # We have some predefined books. 
    library.add_book(Book("Python Programming", "John Zelle", 3))
    library.add_book(Book("Clean Code", "Robert C. Martin", 2))
    library.add_book(Book("The Pragmatic Programmer", "Andy Hunt", 4))
    library.add_book(Book("Artificial Intelligence", "Stuart Russell", 2))
    library.add_book(Book("Machine Learning", "Tom Mitchell", 5))

    users = {
        "admin": Admin("admin"),
        "shubham": User("shubham"),
        "neha": User("neha")
    }

    print("🔐 Welcome to the Advanced Library Management System")
    username = input("Enter your username (admin/shubham/neha): ").strip()

    if username not in users:
        print("❌ Invalid user.")
        return

    current_user = users[username]
    print(f"\n👋 Welcome, {current_user.username}!")

    while True:
        print("\n💡 Options:")
        if isinstance(current_user, Admin):
            print(" 1. Add Book")
        print(" 2. View Available Books")
        print(" 3. Borrow Book")
        print(" 4. Return Book")
        print(" 5. View My Borrowed Books")
        print(" 6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1" and isinstance(current_user, Admin):
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            current_user.add_book(library, title, author, copies)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter the title of the book to borrow: ")
            current_user.borrow_book(library, title)

        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            current_user.return_book(library, title)

        elif choice == "5":
            current_user.view_my_books(library)

        elif choice == "6":
            print("👋 Thank you for using the Library Management System.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
