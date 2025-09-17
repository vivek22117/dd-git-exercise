class Book:
    def __init__(self, title:str, author:str, book_id:str):
        self.title = title
        self.author= author
        self.book_id = book_id
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out= True

    def check_in(self):
        self.is_checked_out = False

    def display(self):
         status = "Not Available" if self.is_checked_out else "Available"
         return(f"Title :{self.title}, author : {self.author}, book_id : {self.book_id}, status : {status}")

class Member:
  def __init__(self, name:str, member_id:str):
    self.name = name
    self.member_id = member_id
    self.borrowed_books : list[Book] = []

  def borrow_book(self, book):
    self.borrowed_books.append(book)
    # print(self.borrowed_books)

  def return_book(self, book):
    self.borrowed_books.remove(book)
    #print(self.borrowed_books)

  def display(self):
    print(f"name : {self.name}, member_id : {self.member_id}, borrowed_book : {self.borrowed_books}")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        self.books[book.book_id] = book #adding book_id as key and book as value in self.books dict

    def register_member(self, member):
        self.members[member.member_id] =member.name #adding member_id as key and member.name as value in self.member dict

    def check_out_book(self,member, book):
         {member.member_id} and {book.book_id} #adding member_id attribute from member instance  and book_d attribute from  book instance
         if not book.is_checked_out:
                book.check_out()
                member.borrow_book(book.title)
                print(f"{member.name} checks out '{book.title}' .")
         else:
                print(f"'{book.title}' is alraedy checked out.")
    
    def book_return(self, member, book):
        book.is_checked_out = False
        member.return_book(book.title)
        print(f"'{book.title}' returned by {member.name} .")

    def display_available_books(self):
        for key,val in self.books.items():
            print(val.display())
        
        
lib = Library()

book1 = Book("The Hobbit", "J.R.R. Tolkien", "9780345339683")
book2 = Book("Dune", "Frank Herbert", "9780441013593")
book3 = Book("1984", "George Orwell", "9780451524935")

member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

# print(lib.books)
lib.register_member(member1)
lib.register_member(member2)

# 4. Show available books
print("--- Available Books ---")
lib.display_available_books()
print("-" * 25)

# 5. Simulate book check-outs
print("--- Checking out books ---")
lib.check_out_book(member1, book1) # Alice checks out The Hobbit
lib.check_out_book(member2, book2)
lib.check_out_book(member1, book2)
# lib.check_out_book("M001", "9780345339683") # Alice checks out The Hobbit
# lib.check_out_book("M002", "9780441013593") # Bob checks out Dune
# lib.check_out_book("M001", "9780441013593") # Alice tries to check out Dune (already checked out)
print("-" * 25)

# 6. Show available books again
print("--- Available Books after check-outs ---")
lib.display_available_books()
print("-" * 25)

# 7. Display member info
print("--- Member Details ---")
member1.display()
member2.display()
print("-" * 25)

# 8. Simulate a book return
print("--- Returning a book ---")
lib.book_return(member1, book1) # Alice returns The Hobbit
print("-" * 25)

# 9. Final check of available books and member info
print("--- Final Status ---")
lib.display_available_books()
member1.display()



























# print(lib.members)
# print("______________________________")
# print(lib.books)
# # print(book1.title)
# print("______________________________")
# lib.check_out_book(member1,book1)
# # print(member1.borrowed_books)
# book1.display()
# member1.display()
# lib.book_return(member1, book1)

# book1.display()
# member1.display()