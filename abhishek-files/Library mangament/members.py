import book
class Members:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books= []
        # boj = self.borrowed_books[title]

    def borrow_book(self,book):
        self.borrowed_books.append(book)
    def return_book(self,book):
        self.borrowed_books.remove(book)
    def display(self):
        print(f"member name : {self.name} ,member Id: {self.member_id} ,Borrowed Book : { self.borrowed_books}")