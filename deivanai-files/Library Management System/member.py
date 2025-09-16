from book import Book

class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrwed_books = []
    def borrow_book(self,book):
        self.borrwed_books.append(book.title)
        print(f"{book.title} added to borrowed list of {self.name}.")

    def return_book(self,book):
        self.borrwed_books.remove(book)
        print(f"{book.title} Removed from borrwed list {self.name},")
    def display(self):
        print(f"INFO \nMember: {self.name}  \nmember_id:{self.member_id}  \nBorrowed book :{self.borrwed_books}")
           
            
            

            
