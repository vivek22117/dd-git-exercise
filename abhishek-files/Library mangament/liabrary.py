class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        return(f"{self.books} is added to the Library.")
       
    def register_member(self,member):
        self.members[member.member_id]=member
        return(f"{self.members[member.member_id].name} registered.")

    def check_out_book(self,member_id ,book_id):
        boj = self.books[book_id]
        moj = self.members[member_id]
       
        if not boj.is_checked_out:
            boj.check_out()
            moj.borrow_book(boj.title)

            print(f"{boj.title} checked out by {moj.name}")
        else:            
            print(f"{boj.title} is already checked out ")

    def return_book(self,member_id,book_id):
        boj = self.books[book_id]
        moj = self.members[member_id]
        boj.is_checked_out = False
        moj.return_book(boj.title)
        print(f"{boj.title}  returned by {moj.name} .")

    def display_available_books(self):
        for key,val in self.books.items():
          if not val.is_checked_out:
            print(val.display())