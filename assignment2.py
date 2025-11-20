# -------------------------------------------------------
# Name: uday vijay
# Date: 18/11/2025
# Project: Library Managment System
# -------------------------------------------------------

books = {}
borrowed = {}

# -------------------------
# FUNCTION: Add Book
# -------------------------
def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter number of copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print("Book added successfully!\n")

# -------------------------
# FUNCTION: View Books
# -------------------------
def view_books():
    print("\n--- Book List ---")
    print("ID\tTitle\t\tAuthor\t\tCopies")
    print("----------------------------------------------")

    for book_id, info in books.items():
        print(f"{book_id}\t{info['title']}\t{info['author']}\t{info['copies']}")
    print()

# -------------------------
# FUNCTION: Search Book
# -------------------------
def search_book():
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title")
    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("Book Found!")
            print(books[book_id])
        else:
            print("Book Not Found")
    
    elif choice == "2":
        title = input("Enter part of title: ").lower()
        found = False
        for book_id, info in books.items():
            if title in info["title"].lower():
                print(f"Book Found: {book_id} -> {info}")
                found = True
        if not found:
            print("No matching book found")
    print()

# -------------------------
# FUNCTION: Borrow Book
# -------------------------
def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed[student] = book_id
            print("Book borrowed successfully!")
        else:
            print("Sorry, no copies available.")
    else:
        print("Invalid Book ID.")
    print()

# -------------------------
# FUNCTION: Return Book
# -------------------------
def return_book():
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if student in borrowed and borrowed[student] == book_id:
        books[book_id]["copies"] += 1
        del borrowed[student]
        print("Book returned successfully!")
    else:
        print("No such borrowing record found.")
    
    # list comprehension for borrowed list
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("\nBorrowed Books List:")
    for item in borrowed_list:
        print(item)
    print()

# -------------------------
# MAIN PROGRAM LOOP
# -------------------------
def menu():
    while True:
        print("====================================")
        print("  Welcome to Library Manager System ")
        print("====================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you! Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run the program
menu()



