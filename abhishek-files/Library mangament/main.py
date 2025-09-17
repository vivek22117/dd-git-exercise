from book  import Book
from members import Members
from liabrary import Library

# --- Main Program ---

# 1. Create a Library instance
my_library = Library()  # books = {}   members = {}

# 2. Create some Book instances and add them to the library
book1 = Book("The Hobbit", "J.R.R. Tolkien", "9780345339683")
book2 = Book("Dune", "Frank Herbert", "9780441013593" )
book3 = Book("1984", "George Orwell", "9780451524935")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# 3. Create some Member instances and register them
member1 = Members(" Alice", "M001")
member2 = Members("Bob", "M002")

my_library.register_member(member1)
my_library.register_member(member2)

# # 4. Show available books
print("--- Available Books ---")
my_library.display_available_books()
print("-" * 25)

# # 5. Simulate book check-outs
# print("--- Checking out books ---")
my_library.check_out_book("M001", "9780345339683") # Alice checks out The Hobbit
my_library.check_out_book("M002", "9780441013593") # Bob checks out Dune
my_library.check_out_book("M001", "9780441013593") # Alice tries to check out Dune (already checked out)
# # print("-" * 25)

# 6. Show available books again
print("--- Available Books after check-outs ---")
my_library.display_available_books()
print("-" * 25)

# 7. Display member info
print("--- Member Details ---")
member1.display()
member2.display()
print("-" * 25)

# 8. Simulate a book return
print("--- Returning a book ---")
my_library.return_book("M001", "9780345339683") # Alice returns The Hobbit
print("-" * 25)

# 9. Final check of available books and member info
print("--- Final Status ---")
my_library.display_available_books()
member1.display()