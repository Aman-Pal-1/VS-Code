#Q1

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
        
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# a = TwoDVector(1,2)
# b = ThreeDVector(1,2,3)
# a.show()
# b.show()



#Q2


# class animals:
#     pass
# class pets(animals):
#     pass
# class Dog(pets):
#     @staticmethod
#     def bark():
#         print("bow bow!!!")
    
# d =Dog()
# d.bark()



#Q3




# class Employee:
#     salary = 234909090
# e = Employee()
# salary = 234909090
# e.increment = 20
# print(e.salary)
# print(e.increment)



#    or



# class Employee:
#     salary = 234909090
#     increment = 20
    
# e = Employee()

# print(e.salary)
# print(e.increment)


# class Employee:
#     salary = 1000000000
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + (self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, updated_salary):
#         self.increment = ((updated_salary/self.salary)-1)*100


# e = Employee()

# print(e.salary)
# print(e.increment)
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 1000000000000
# print(e.increment)



#Q4



# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real = self.r * c2.r - self.i * c2.i
#         imaginary = self.r * c2.i + self.i * c2.r
#         return Complex(real, imaginary)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)

# # Testing addition
# print("Sum:", c1 + c2)

# # Testing multiplication
# print("Product:", c1 * c2)




#Q5


# class vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def __add__(self,other):
#         result = vector(self.x + other.x , self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self,other):
#         result = self.x * other.x , self.y * other.y, self.z * other.z
#         return result

#     def __str__(self):
#         return f"Vector({self.x},{self.y},{self.z})"
    
# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# v3 = vector(7,8,9)

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)



#Q6



# class vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def __add__(self,other):
#         result = vector(self.x + other.x , self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self,other):
#         result = self.x * other.x , self.y * other.y, self.z * other.z
#         return result

#     def __str__(self):
#         return f"Vector({self.x}i + {self.y}j + {self.z}k)"
    
# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# v3 = vector(7,8,9)

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)




#Q7



class vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
v1 = vector([1,2,3])
print(len(v1))

