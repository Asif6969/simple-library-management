class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} (Book ID: {self.book_id}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_book = []

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_book.append(book)
            print(f"{self.name} borrowed {book.title}")

        else:
            print(f"{book.title} is already checked out")

    def return_book(self, book):
        if book in self.borrowed_book:
            if book.return_book():
                self.borrowed_book.remove(book)
                print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title}")

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.title} from library")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print("Book not found")
        return None

class Librarian(Member):
    def __init__(self, name, member_id, employee_id):
        super().__init__(name, member_id)
        self.employee_id = employee_id

    def add_book_to_library(self, book, library):
        library.add_book(book)

    def remove_book_from_library(self, book, library):
        library.remove_book(book)

    def __str__(self):
        return f"Librarian: {self.name} (Employee id: {self.employee_id}"

#-----------------------------------------------------------------------------------

library1 = Library()
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9876543210")
member1 = Member("Asif", "M0001")
librarian1 = Librarian("Jake", "M0002", "E001)")

library1.add_book(book1)
librarian1.add_book_to_library(book2, library1)
library1.register_member(member1)

print(librarian1)
print(member1)

member1.borrow_book(book1)
print(book1)
member1.return_book(book1)
print(book1)