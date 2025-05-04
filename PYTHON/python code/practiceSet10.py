#q1

# class programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = programmer("Uditya",10000000000,206246)
# print(p.name,p.salary,p.pin,p.company)
# r=programmer("Aman",10000000000000,206246)
# print(r.name,r.salary,r.pin,r.company)



#q2

# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"The Square is {self.n*self.n}")
#     def cube(self):
#         print(f"The Cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The Squareroot is {self.n**1/2}")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()



#q3

# class Demo:
#     a = 4

# o = Demo()
# print(o.a) # prints the class attribute because instance attribute is not present
# o.a = 0 # Instance attribute is set 
# print(o.a) # prints the instance attribute because instance attribute is present
# print(Demo.a) # prints the class attribute



#q4

# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"The Square is {self.n*self.n}")
#     def cube(self):
#         print(f"The Cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The Squareroot is {self.n**1/2}")
    
#     @staticmethod
#     def hello():
#         print("Hello world!")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()
# a.hello()




#q5

# from random import randint

# class Train:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
#     def getStatus(self):
#         print(f"Train no. {self.trainNo} is running on time")
        
#     def getFare(self, fro, to):
#         fare = randint(222, 5555)
#         print(f"Ticket for train no: {self.trainNo} from {fro} to {to} costs {fare}")

# # Usage example:
# t = Train(12399)
# t.book("Rampur", "Delhi")
# t.getStatus()
# t.getFare("Rampur", "Delhi")



#q6

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
        
    def getStatus(slf):
        print(f"Train no. {slf.trainNo} is running on time")
        
    def getFare(slf, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket for train no: {slf.trainNo} from {fro} to {to} costs {fare}")

# Usage example:
t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
