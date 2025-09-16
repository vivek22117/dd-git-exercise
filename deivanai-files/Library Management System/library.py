from book import Book
from member import Member

class Library:

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def check_out_book(self,member_id,book_id):
        member = self.members[member_id]
        book   = self.books[book_id]
        if not book.is_checked_out:
            book.check_out()
            member.borrow_book(book)
            print(f"Book {book.title} was issued to {member.name} .")
        else:
            print("Book not available.") 
    def return_book(self,member_id,book_id):
         member = self.members[member_id]
         book   = self.books[book_id]
         member.borrwed_books.remove(book.title)  
         book.is_checked_out = False
         print(f"{book.title} returned by {member.name}")
                 

                     


    def display_available_books(self):
        for key, val in (self.books).items():
            val.display()

                



