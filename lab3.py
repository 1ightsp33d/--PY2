from dataclasses import dataclass
import inspect
@dataclass(frozen=True)
#bucle your seatbelt Dorothy, cause Kansas is going bye-bye...
class Book:
    def __init__(self,name:str,author:str):
            self.name=name
            self.author=author
    def __str__(self)->str:
            return self.name+self.author
    def __repr__(self)->list:
            return (self.name,self,author)

class Audio_book(Book):
    def __init__(self,name:str,author:str,duration:float):
        Book.__init__(self,name,author)
        if duration<=0:
            raise ValueError("negative page number")
        self.duration=duration
    def __repr__(self):
            return (''.join([str(getattr(self,ob))+";" for ob in dir(self) if not ob.startswith("_")]))

class Paper_book(Book):
    def __init__(self,name:str,author:str,pages:int):
        Book.__init__(self,name,author)
        if pages<=0:
            raise ValueError("negative page number")
        self.pages=pages
    def __repr__(self):
            return (''.join([str(getattr(self,ob))+";" for ob in dir(self) if not ob.startswith("_")]))
