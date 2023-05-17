"""

what we need:=

library:-
books :list of books
active: id of the book

book:-
id:int
title:str
pages: list of pages
ActivePageNumber: int

pages:-
pageId
text


"""

pagesDic = [a for i,a in enumerate("abcdefghijklmnopqrstuvwxyz")]
#print(pages)

class Pages:
    def __init__(self,key,text):
        
        self.pageId = key
        self.text = text
        


class Book:
    def __init__(self,title,pages):
        self.id = None
        self.title = title
        self.activePageId = 0
        dic = {}
        for i in pages:
            dic[len(dic.keys())] = i
        self.pages =dic



class Library:
    def __init__(self):
        self.books = [Book]
        self.active:Book = None


    def addBook(self,title,pages):

        bookEntity = Book(title,pages)
        bookEntity.id = len(self.books)
        self.books.append(bookEntity)
        
        print(self.books)

    def getBook(self,no,pageNo):
        currActive = self.active
        if currActive:
            currActive = None
        book = self.books[1]
        self.active = book
        book.activePageId = pageNo
        
        return book.pages[pageNo]

    def turnPage(self):
        currActive = self.active
        if currActive:
            currActive = None
        book = self.active
        book.activePageId += 2
        print(book.pages[book.activePageId])
        return book.pages[book.activePageId]
        
       

c = Library()
c.addBook("abc",pagesDic)
c.getBook(0,5)
c.turnPage()