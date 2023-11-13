# 1.Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle, Rectangle, and Triangle.
#  Implement methods to calculate area and perimeter for each shape.
import math
from typing import Any
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(Shape):
    def __init__(self, a,b,c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c

circle = Circle(5)
rectangle = Rectangle(12,5)
triangle = Triangle(3,4,2)
print(circle.area(),circle.perimeter())
print(rectangle.area(),rectangle.perimeter())
print(triangle.area(),triangle.perimeter())

# 2.Design a bank account system with a base class Account and subclasses SavingsAccount 
# and CheckingAccount. Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    def get_balance(self):
        return self.balance
    def interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def interest(self):
        self.balance +=  self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance,fee):
        super().__init__(balance)
        self.fee = fee
    def withdraw(self, amount):
        if self.balance >= amount + self.fee:
            self.balance -= (amount + self.fee)

savings = SavingsAccount(1000,0.03)
print(savings.get_balance())
savings.withdraw(500)
print(savings.get_balance())
savings.interest()
print(savings.get_balance())
checking = CheckingAccount(1000,10)
checking.deposit(200)
checking.withdraw(500)
print(checking.get_balance())

# 3.Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types of vehicles like Car, Motorcycle,
#  and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def mileage(self):
        pass
    def towing_capacity(self): 
        pass

class Car(Vehicle):
    def calculate_mileage(self, miles,fuel):
        mileage = miles/fuel
        return mileage
    
class Motorcycle(Vehicle):
    def calculate_mileage(self, miles,fuel):
        mileage = miles/fuel
        return mileage
    
class Truck(Vehicle):
    
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity
    
    def get_towing_capacity(self):
        return self.towing_capacity
    
    def calculate_mileage(self, miles,fuel):
        mileage = miles/fuel
        return mileage

car = Car("Toyota","Camry",2020)
motorcycle = Motorcycle("Honda","CBR",2021)
truck = Truck("Ford","F-150",2022,5000)

print(car.calculate_mileage(100,8))
print(motorcycle.calculate_mileage(124,9))
print(truck.get_towing_capacity())

# 4.Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
# Each subclass should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_salary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def get_department(self):
        return self.department
    def assign_task(self, task):
        print(f"Manager {self.name} assigned task: {task} to the team.")

class Engineer(Employee):
    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill
    def get_skill(self):
        return self.skill
    def engineer_skill(self):
        return f"{self.name} has {self.skill} skill"

class Salesperson(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission
    def get_commission(self):
        return self.commission
    def make_sale(self, sale):
        win = sale * self.commission
        return f"{self.name} made a sale of {sale} and won {win} dollars"

manager = Manager("John Doe", 50000, "Sales")
engineer = Engineer("Jane Smith", 60000, "Python")
salesperson = Salesperson("Bob Johnson", 70000, 0.07)
print(manager.assign_task("Sell products"))
print(engineer.engineer_skill())
print(salesperson.make_sale(1000))

# 5.Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and Fish. 
# Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species

class Mammal(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def get_breed(self):
        return self.breed
    def run(self):
        return f"{self.name} is running"

class Bird(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color
    def get_color(self):
        return self.color
    def fly(self):
        return f"{self.name} is flying"
    
class Fish(Animal):
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size
    def get_size(self):
        return self.size
    def swim(self):
        return f"{self.name} is swimming"

#Example of usage

mammal = Mammal("Lion", "Mammal", "Lioness")
bird = Bird("Eagle", "Bird", "Red")
fish = Fish("Clownfish", "Fish", "Small")

print(mammal.get_name())
print(mammal.run())
print(bird.fly())
print(bird.get_color())
print(fish.swim())

# 6.Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD, and Magazine. 
# Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self,title,year):
        self.title = title
        self.year = year

class Book(LibraryItem):
    def __init__(self,title,year,author,genre):
        super().__init__(title,year)
        self.author = author
        self.genre = genre
    def display_info(self):
        return f"{self.title} ({self.year}) by {self.author} has a genre of {self.genre}."

class DVD(LibraryItem):
    def __init__(self,title,year,director,duration,genre):
        super().__init__(title,year)
        self.director = director
        self.duration = duration
        self.genre = genre
    def display_info(self):
        return f"{self.title} ({self.year}) by {self.director} has a duration of {self.duration} minutes and is a {self.genre}."

class Magazine(LibraryItem):
    def __init__(self,title,year,publisher,genre,pages):
        super().__init__(title,year)
        self.publisher = publisher
        self.genre = genre
        self.pages = pages    
    def display_info(self):
        return f"{self.title} ({self.year}) by {self.publisher} has {self.pages} pages and is a {self.genre} magazine."
    

book = Book("The Hobbit", 1937, "J.R.R. Tolkien", "Fantasy")
dvd = DVD("The Lord of the Rings", 2001, "Peter Jackson", 110, "Fantasy")
magazine = Magazine("The Atlantic", 2020, "The Atlantic", "News", 100)
print(book.display_info())
print(dvd.display_info())
print(magazine.display_info())