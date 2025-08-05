class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"✅ '{title}' by {author} added to the library.")

    def display_books(self):
        print("\n📚 Library Books:")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(f" - {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"✅ You borrowed '{book.title}'")
                return
        print("❌ Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"✅ You returned '{book.title}'")
                return
        print("❌ You didn’t borrow this book or wrong title.")


def main():
    library = Library()

    # We store some books 
    library.add_book("Python Basics", "John Doe")
    library.add_book("Learning AI", "Jane Smith")
    library.add_book("Machine Learning 101", "Andrew Ng")
    library.add_book("Clean Code", "Robert C. Martin")
    library.add_book("Data Science Handbook", "Jake VanderPlas")

    while True:
        print("\n📖 Library Menu:")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "5":
            print("👋 Exiting. Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
