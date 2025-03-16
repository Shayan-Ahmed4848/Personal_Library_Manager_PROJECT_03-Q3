library = []

def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    
    if not title or not author or not year.isdigit() or not genre or read_status not in ("yes", "no"):
        print("Invalid input. Please enter valid details.")
        return
    
    library.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status == "yes"
    })
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book():
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice.")
        return
    
    keyword = input("Enter search term: ").strip().lower()
    results = [book for book in library if (choice == "1" and keyword in book["title"].lower()) or (choice == "2" and keyword in book["author"].lower())]
    
    if results:
        print("\nMatching Books:")
        for idx, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books():
    if not library:
        print("Your library is empty.")
        return
    
    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics():
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100 if total_books else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
