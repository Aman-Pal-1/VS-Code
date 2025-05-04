# class Employee:  # base class
#     company = "Infosys"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

# # class programmer:
# #     company = "ITC Infotech"
# #     def show(self):
# #         print(f"The name is {self.name} and the salary is {self.salary}")  

# #         def showLang(self):
# #             print(f"The name is {self.name} and the salary is {self.salary}")  

# class programmer(Employee):  # Derived Class or child class
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")  


# a = Employee()
# b = programmer()

# print(a.company, b.company)


#types of inheritance are --- 1> single inheritance       2> multiple inheritance     




#     multiple inheritance     

class Employee:  # base class
    company = "Infosys"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the language here is Your Language: {self.language}")


class programmer(Employee, coder):  # Derived Class or child class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.language}")  


a = Employee()
b = programmer()
b.show()
b.printLanguages()
b.showLanguage()

print(a.company, b.company)

