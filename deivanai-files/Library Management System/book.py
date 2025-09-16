class Book:
    def __init__(self,title,author,book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_checked_out = False
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checking out book")
        else:
             print(f"{self.title} already checked out book")
    def check_in(self):
        if self.is_checked_out:
            self.check_out = False
            print(f"{self.title} has been checked in ")
        else:
            print(f"{self.title} is available")
    def display(self):

        print(f"Title : {self.title} \nAuthor : {self.author} \nBook_id : {self.book_id} \nStatus : {'Not Available' if self.is_checked_out else 'Available'} .")



