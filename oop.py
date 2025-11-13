# Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code 
# around objects rather than functions and logic.It focuses on creating reusable and modular code by grouping 
# related data (attributes) and behavior (methods) into self-contained units called objects.
# Key Concepts:
# Classes: A class acts as a blueprint or a template for creating objects. It defines the structure and 
# behavior that objects of that class will possess. For example, a Dog class would define attributes 
# like name and age, and methods like bark() and fetch().


class Dog:
    species = "Canis familiaris"  # Class attribute

    def _init_(self, name, age, color):
            self.name = name  # Instance attribute
            self.age = age    # Instance attribute
            self.color = color    # Instance attribute

    def bark(self):
            return f"{self.name} says Woof!"
    
# Objects (Instances): An object is a concrete instance of a class. When you create an object from a class,
# you are instantiating that class. Each object has its own set of specific values for the attributes defined in the class.
# Python

mr_tobi_dog = Dog("Jack", 3, "brown")  # Creating an object (instance) of the Dog class
mic_dog = Dog("Lucy", 5, "white")  # Creating an object (instance) of the Dog class
alex_dog = Dog("Hero", 2, "Yellow")  # Creating an object (instance) of the Dog class
demola_dog = Dog("Ekuke", 4, "Black")  # Creating an object (instance) of the Dog class

# Attributes: Attributes are variables associated with an object or a class.
# Instance attributes: are unique to each object and are defined within the _init_ method using self.attribute_name.
# Class attributes: are shared among all instances of a class and are defined directly within the class body, outside of any methods.

print(mic_dog.name)  # Accessing an instance attribute
print(demola_dog.name)
print(mic_dog.color)
print(alex_dog.name, alex_dog.color)
print(alex_dog)

# Methods: Methods are functions defined within a class that operate on the object's data. 
# They define the actions or behaviors an object can perform. The self parameter in a method refers to the 
# instance of the class on which the method is being called.


# print(my_dog.bark())  # Calling a method on an object



# Parent class (Base class)
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class (Derived class) inheriting from Animal
class Dog(Animal):
    def _init_(self, name, breed):
        super()._init_(name)  # Call the parent class's constructor
        self.breed = breed

    # Method overriding: Providing a specific implementation for 'speak'
    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

# Another Child class
class Cat(Animal):
    # Method overriding
    def speak(self):
        return f"{self.name} the cat says Meow!"

# Another Child class
class Monkey(Animal):
    # Method overriding
    def speak(self):
        return f"{self.name} the monkey says hauhau!"

# Another Child class
class Snake(Animal):
    # Method overriding
    def speak(self):
        return f"{self.name} the snake says ssssh!"

# Create instances and demonstrate behavior
generic_animal = Animal("Creature")
print(generic_animal.speak())

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())

my_cat = Cat("Whiskers")
print(my_cat.speak())

my_monkey = Monkey("brude")
print(my_monkey.speak())

my_snake = Snake("Paramole")
print(my_snake.speak())