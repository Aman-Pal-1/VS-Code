class Employee:
    lang="python"  # This is a Class Attribute.
    salary=1200000000

    def getinfo(self):
        print(f"The Language is {self.lang} the salary is {self.salary}")

    # @staticmethod  #when we use @staticmethod then we not give any object in function.
    # def greet():
    #     print("Good Morning")

def __init__(self, name, salary, language):
    print(f"The language is {self.language}.The salary is {self.salary}") # dunder method which is automatically called
    self.name= name
    self.salary = salary
    self.language = language
    print("I am creating an object")

Uditya = Employee("Uditya",13000000000,"javascript")





Uditya.name = "Uditya_Pal" # this is an object attribute.
# Uditya.lang = "JavaScript" # This is an Instance Attribute.
# print(Uditya.lang,Uditya.salary)

# Employee.greet(Uditya)


Uditya.getinfo()  # both are same
Employee.getinfo(Uditya) # both are same
