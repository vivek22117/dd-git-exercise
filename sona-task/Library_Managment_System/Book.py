
class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.is_checked_out=False
        
    def check_out(self):
        self.is_checked_out=True
        
    def check_in(self):
        self.is_checked_out=False
        
    def display(self):
        status="Checkout Out" if self.is_checked_out else "Available"
        return(f"Title:{self.title} ,Author :{self.author} , BookId:{self.book_id} ,Status: {status}")
        

