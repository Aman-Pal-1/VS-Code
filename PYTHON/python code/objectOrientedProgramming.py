# class

# class Employee:
#     name="Uditya_Pal"
#     lang="python"
#     salary=1200000000

# Aman= Employee()
# print(Aman.name,Aman.salary)


class Employee:
    lang="python"  # this is a class attribute.
    salary=1200000000

Aman = Employee()
print(Aman.lang,Aman.salary)

Uditya = Employee()
Uditya.name = "Uditya_Pal" # this is an object attribute.
print(Uditya.name,Uditya.lang,Uditya.salary)

Ashwani = Employee()
print(Ashwani.lang,Ashwani.salary)

Gagan = Employee()
print(Gagan.lang,Gagan.salary)

Nainsi = Employee()
print(Nainsi.lang,Nainsi.salary)

neeraj = Employee()
print(neeraj.lang,neeraj.salary)

# Here name is object attribute and salary and language are class attributes and they directly belong to the class.
