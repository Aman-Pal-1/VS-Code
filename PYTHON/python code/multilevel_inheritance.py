# class Employee:
#     a = 1

# class Programmer(Employee):
#     b = 2
# class Manager(Programmer):
#     c = 3

# o = Employee()
# print(o.a)
# # print(o.b)

# o = Programmer()
# print(o.a,o.b)

# o = Manager()
# print(o.a,o.b,o.c)


# Super Method


# class Employee:
#     def __init__(self):
#        print("Constructor of Employee") 
#     a = 1

# class Programmer(Employee):
#     def __init__(self):
#        print("Constructor of Employee") 
#     b = 2
# class Manager(Programmer):
#     def __init__(self):
#        super ().__init__()
#        print("Constructor of Employee") 
#     c = 3

# o = Employee()
# print(o.a)
# # print(o.b)

# o = Programmer()
# print(o.a,o.b)

# o = Manager()
# print(o.a,o.b,o.c)



#   Class Method



# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"It Class Attribute of a is {cls.a}")

# e= Employee()
# e.a = 45
# e.show()


# Property decorators


# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"It Class Attribute of a is {cls.a}")

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e= Employee()
# e.a = 45
# e.show()
# e.name = "Uditya Pal"
# print(e.fname,e.lname)


#   operator OverLoading

class Num:
    def __init__(self,n):
        self.n = n
    
    def __add__(self,num):
        return self.n + num.n

n = Num(1)
m = Num(2)

print(n + m)