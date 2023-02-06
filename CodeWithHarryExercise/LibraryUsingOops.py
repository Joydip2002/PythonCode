class Library:
    no_Of_Books = 0
    Book_Name = []
   
    def addBook(self,book_Name):
        self.Book_Name.append(book_Name)
        self.no_Of_Books += 1

    def getBook(self):
        print(f"Available Book in Library:\n{self.Book_Name}")

    def total_No_Of_Books(self):
        print(f"Total No Of Books: {len(self.Book_Name)}")

obj = Library()

obj.addBook("DSA")
obj.addBook("Networking")
obj.addBook("OS")
obj.addBook("DBMS")

obj.getBook()

obj.total_No_Of_Books()

# When Program is stopped the list of books empty.These Added books are not loaded in the memory.