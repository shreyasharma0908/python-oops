# # 04/11/26

# # Abstractmethod

# from abc import ABC,abstractmethod

# class Payment (ABC):    #parent abstract class

#     @abstractmethod
#     def pay (self,amount):
#         pass

# class CreditCard(Payment):

#     def pay (self,amount):
#         print("Paid",amount,"using CreditCard")

# class Cash(Payment):

#     def pay(self,amount):
#          print("Paid",amount,"using Cash")
    
# class UPI(Payment):

#     def pay(self,amount):
#          print("Paid",amount,"using UPI")
       

# p1=UPI()
# p1.pay(1000)

# p2=CreditCard()
# p2.pay(2000)

# p3=Cash()
# p3.pay(3000)


# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def drive(self):
#         pass

# class Bike (Vehicle):

#     def drive(self):
#         print("bike is moving")

# class Car (Vehicle):

#     def drive(self):
#         print("Car is moving")

# class Bus(Vehicle):

#     def drive(self):
#         print("Bus is moving")

# car=Car()
# car.drive()

# bike=Bike()
# bike.drive()

# bus=Bus()
# bus.drive()


# from abc import ABC, abstractmethod
# import math

# # Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# # Circle Class
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius


# # Rectangle Class
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# # Square Class
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side


# # Creating Objects
# c = Circle(45)
# r = Rectangle(1, 4)
# s = Square(9)

# # Display Areas
# print("Area of Circle =", round(c.area(), 2))
# print("Area of Rectangle =", r.area())
# print("Area of Square =", s.area())



# Bank Account (Abstract Class)

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass


class SavingsAccount(BankAccount):

    def deposit(self,amount):
        print("Saving Account: deposited", amount)

    def withdraw(self,amount):
        print("Saving Account: withdraw ", amount)


class CurrentAccount(BankAccount):

    def deposit(self,amount):
         print("Current Account: deposited", amount)
    
    def withdraw(self,amount):
         print("Cureent Account: withdraw ", amount)
    

s = SavingsAccount()
s.deposit(5000)
s.withdraw(1000)

c = CurrentAccount()
c.deposit(6000)
c.withdraw(5500)


# Notification System


# from abc import ABC, abstractmethod

# class Notification(ABC):

#     @abstractmethod
#     def send(self):
#         pass


# class EmailNotification(Notification):

#     def send(self):
#         print("Sending notification through Email")


# class SMSNotification(Notification):

#     def send(self):
#         print("Sending notification through SMS")


# class WhatsAppNotification(Notification):

#     def send(self):
#         print("Sending notification through WhatsApp")


# e = EmailNotification()
# e.send()

# s = SMSNotification()
# s.send()

# w = WhatsAppNotification()
# w.send()


# Institute Management
# from abc import ABC, abstractmethod

# class Person(ABC):

#     @abstractmethod
#     def display_details(self):
#         pass


# class Student(Person):

#     def display_details(self):
#         print("Student Name: Shreya")
#         print("Course: AIPA")


# class Teacher(Person):

#     def display_details(self):
#         print("Teacher Name: Shailesh yadav")
#         print("Subject: Python")


# class Principal(Person):

#     def display_details(self):
#         print("Principal Name: Ajay Pal Singh")
#         print("Department: Institute")


# s = Student()
# s.display_details()

# print()

# t = Teacher()
# t.display_details()

# print()

# p = Principal()
# p.display_details()

