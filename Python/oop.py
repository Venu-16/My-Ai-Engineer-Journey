"""
OOP in Python:
to map with real worlds scenarios, we started using objects in code.
this is called oop.
"""

"""
Class & Object in python:
#creating class
class Student:
    name = "venu Madhav"
    
#creating object (Instance)
s1 = Student()
print(s1.name)
    
"""

class Student:
    name = "Venu Madhav"

s1 = Student()
print(s1.name)

class Car:
    color = "blue"
    brand = "benz"

c1 = Car()
print(c1.color,c1.brand)

#init function
class Student:
    name = "Venu Madhav"
    def __init__(self,name):
        self.name = name
        print("do some work")

s2 = Student("venu")
print(s2.name)

"""Class & Instance Attributes
Class.attr
obj.attr
"""
class Student:
    college_name = "mohan Babu University"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Venu Madhav",99)
s1.welcome()
print(s1.get_marks())

"""
 Static methods:
 class Student:
    @static method #decorator
    def college():
        print("Abc") 
Decorators allow us to wrap another function in order to extend the behavior
of the wrapped function, without permanently modifying it.
"""

class Student:
    college_name = "Mohan Babu University"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")

s1 = Student("Venu Madhav",99)
s1.hello()

"""
Abstraction :
Hiding the implementation details of a class and
only showing the essential features to the user.

Encapsulation:
Wrapping data and function into a single unit.
"""
#Abstraction

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False
    def start(self):
        self.cluth = True
        self.acc = True
        print("vroom vroom.....")
c = car()
c.start()


#del Keyword
#Used to delete object properties or object itself
del s1.name
del s1
#print(s1) #returns error

#Private(like) attributes & methods
"""
private attributes & methods are meant to be used only within the
class and are not accessible from outside the class."""

class Account:
    def __init__(self, acc_no, acc_pas):
        self.acc_no = acc_no
        self.__acc_pas = acc_pas



acc1 = Account("12345", "cbrfikfj")

print(acc1.acc_no)
#print(acc1.__acc_pas)

# to define anything in private use two underscore before identifiers.

#Inheritance
#when one class derives the properties and methods of another class.
class Car:
    color ="black"
    @staticmethod
    def start():
        print("vroom vroom.....")
    @staticmethod
    def stop():
        print("stopppppp")

class Toyoto(Car):
    def __init__(self,name):
        self.name = name

c1 = Toyoto("fortuner")
c2 = Toyoto("prius")

print(c1.color)

#types ==> 1. Single Inheritance,  2. Multi-level Inheritance,  3. Multiple Inheritance
"""
Single Inheritance:

One child class inherits from a single parent class."""
class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

obj = Child()
obj.display()
obj.show()

"""Multilevel Inheritance:

A class inherits from another class, which in turn inherits from another class."""
class Grandparent:
    def display_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def display_parent(self):
        print("Parent class")

class Child(Parent):
    def display_child(self):
        print("Child class")

obj = Child()
obj.display_grandparent()
obj.display_parent()
obj.display_child()

"""Multiple Inheritance:

A child class inherits from more than one parent class."""

class Father:
    def show_father(self):
        print("Father class")

class Mother:
    def show_mother(self):
        print("Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("Child class")

obj = Child()
obj.show_father()
obj.show_mother()
obj.show_child()

#Class Method
"""A class method is bound to the class & receives the class as an 
implicit first argument.

Note - static method ca't access or modify class state and generally for utility."""

class Student:
    @classmethod
    def college(cls):
        pass


#property
class Student:
    @property
    def college(cls):
        pass

    #polymorphism : Operator overloading
    """
    when the same operator is allowed to have different meaning to the context."""

class Calculator:
    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return a

obj = Calculator()
print(obj.add(2, 3))
print(obj.add(2, 3, 4))

