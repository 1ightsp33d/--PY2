class Book:
    def __init__(self,id:int,name:str,pages:int):
        if (id<=0) or (len(name)==0) or (pages<=0):
                raise ValueError("something is wrong")
        self.id=id
        self.name=name
        self.pages=pages
    def __str__(self):
            return "Книга"+" "+self.name
    def __repr__(self):
        return str(self.id)+";"+self.name+";"+str(self.pages)

class Library:
    def __init__(self,name:str="mylibrary",books:list=[]):
        if False in [isinstance(f,int) for f in books]:
            raise ValueError("non-integer")
        self.books=books
        self.name=name
    def get_next_book_id(self):
        if len(self.books)==0:
                return 1
        else:
                return self.books[-1]+1
    def get_index_by_book_id(self,id):
        try :   
            return self.books.index(id)
        except:
            raise ValueError("no such book")

            
