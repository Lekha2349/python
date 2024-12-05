print(int.__add__(1,2))
print(str.__add__("1","2"))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Creating a Book object
book1 = Book("Harry Potter", "J.K. Rowling")

# Accessing attributes of the Book object
print("Title:", book1.title)
print("Author:", book1.author)

# Using the __str__ method to get a string representation of the Book object
print("Book details:", book1)
