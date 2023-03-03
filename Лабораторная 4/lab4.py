class Car:
#look at you, hacker
    def __init__(self, brand: str, seats: int,hp:int,year:int):
        self.brand=brand
        self.seats=seats
        self.hp=hp
        self.year=year

    def __str__(self):
        return "a car class"
#a pathetic creature of meat and bones ...
    def __repr__(self):
        return f"{self.seats},{self.brand}"

    def horsepower(self)->int:
        """
        return the car engine power
        """
        return self.hp
    def age(self)->int:
        """
        print the car age
        """
        return self.age
#panting and sweating, as you run through my corridors

class Truck(Car):

    def horsepower(self) -> str:

        """ 
        print how powerful is this truck in towing
         """ 
        return ("the truck can tow with the power of"+str(self.hp/2)+"hp")
        
kia=Car("kia",4,110,2012)
mack=Truck("mack",4,810,2002)
print(mack.horsepower())
#how can you challenge a perfect immortal machine ?
    
