import doctest
class person:
    def __init__(self,name:str,age:int,hashn:int,children:list):
        """
        Создание и подготовка к работе объекта "персона"
    
        :param name: имя
        :param age: возраст
        :param hashn: индивидуальный номер
        :param chldren: список индивидуальных номеров детей
        """
        self.name=name
        self.age=age
        self.hashn=hashn
        self.children=children
        self.age+=1
    def increase_age(self):
        """
        функция, увеличивающая значение возраста объекта
        Примеры 
        >>> man=person("John",45,198722,[123456])
        >>> man.increase_age()

        """
        self.age+=1
    def decrease_age(self):
        """
        функция, уменьшающая значение возраста объекта
        :raise ValueError: Если возраст равен нулю
        Примеры 
        >>> man=person("John",45,198722,[123456])
        >>> man.decrease_age()
        """

        if self.age>0:
            self.age-=1
        else:
            raise ValueError("age 0")
    def add_children(self,childn:int):
        """
        добавить ребенка в список
        :raise ValueError: если добавляеымый номер равен номеру исходного объекта, нулю или уже есть в списке
        Примеры 
        >>> man=person("John",45,198722,[123456])
        >>> man.add_children(155277)

        """
        if self.hashn==childn or childn==0 or (childn in self.children):
            raise ValueError("wrong number")

        self.children.append(childn)

class car:
    def __init__(self,brand:str,cost:int):
        """
        Создание и подготовка к работе объекта автомобиля
        :param brand: manufacturer
        :param cost: price
        """ 
        if len(brand)==0:
            raise ValueError("no name")
            self.brand=brand
        if cost<=0:
            raise ValueError("zero or negative cost")
            self.cost=cost
    def change_brand(self,newbrand:str):
        """
        Смена производителя автомобиля
        :raise ValueError: если смена на того же производителя или пустую строку
        """
        if newbrand==self.brand or len(newbrand)==0:
            raise ValueError("same brand")
        self.brand=newbrand
    def increase_price(percent:int):
        """
        повышение цены на percent процентов
        """
        self.cost=round(self.cost*(1+percent))
    def decrease_price(percent:int):
        """
        пониение цены на percent процентов
        """

        self.cost=round(self.cost*(1-percent))
class student:
    def __init__(self,name:str, age:int,grades:list):
        """
        Создание и подготовка к работе объекта ученика
        :param name: имя
        :param age: возраст
        :param grades: оценки
        :raise ValueError: если нецелочисленные оценки
        :raise ValueError: если пустое имя
        :raise ValueError: если возраст неположительный
        """
        if len(name)==0:
            raise ValueError("no name")
        self.name=name
        if False in [isinstance(f,int) for f in grades]:
             raise ValueError("nonint grades")
        self.grades=grades
        if age<=0:
            raise ValueError("wrong age")
        self.age=age
    def add_grades(self,new_grades:list):
        """ 
        Добавление новых оценок
        :raise ValueError: если новые оценки нецелочисленные
        """
        if False in [isinstance(f,int) for f in new_grades]:
             raise ValueError("nonint grades")

        self.grades.extend(new_grades)
    def increase_age(self):
        """
        функция, увеличивающая значение возраста объекта
        """
        self.age+=1
    def decrease_age(self):
        """
        функция, уменьшающая значение возраста объекта
        :raise ValueError: Если возраст равен нулю
        """

        if self.age>0:
            self.age-=1
        else:
            raise ValueError("age 0")

if __name__=="__main__":
    doctest.testmod()
