class Book():
    
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.__price=price # Private Attribute  
        self.price=price
    @property
    
    def price(self):
        return self.__price
    
    @price.setter
    
    def price(self,value):
        if value<0:
            raise ValueError("Price can not be Negative.")
        self.__price=value
    
    def into(self):
        return f"{self.title} by {self.author} and ${self.price:.2f}"
    
    
class Ebook(Book):
    def into(self):
        return f"{super().into()} (Ebook)"

book = Book("Python Basics", "A. Smith", 20)
ebook = Ebook("Python Basics", "A. Smith", 12)
    
print(book.into())
print(ebook.into())

Book.price=34
print(Book.price)

try:
    Book.price = -4672
except ValueError:
    print("Error:")