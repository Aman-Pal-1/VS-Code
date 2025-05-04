#Q1
# def greatest(a,b,c):
#     if (a>b and a>c):
#         print("a is greater than other") 
#         return a 
#     elif(b>a and b>c):
#         print("b is greater than other")
#         return b
#     elif(c>a and c>b):
#         print("c is greater than other")
#         return c
#     elif(a==b or a==c or a==b==c):
#         # print("You give any two or more values are same.")
#         return "You give any two or more values are same."

# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))
# c = int(input("Enter the value of c :"))

# print(greatest(a,b,c))



#Q2
#°F = °C × 9/5 + 32

# def temperature(Fahrenheit):
#     return 5*(Fahrenheit-32)/9
    
# Fahrenheit = float(input("Enter Temperature in Fahrenheit : "))
# celsius = temperature(Fahrenheit)
# print(f"{round(celsius,2)}°C")



#Q3

# print("a")
# print("b")
# print("c")
# print("d",end = "")
# print("e",end = "")



#Q4

'''
sum(1)= 1
sum(2)= 1+2
sum(3)= 1+2+3
sum(4)= 1+2+3+4
sum(5)= 1+2+3+4+5

sum(n)= 1+2+3+4+5....... n
sum(n)= 1+2+3+4+5....... n-1 + n

sum(n)= sum(n-1)+n

'''

# def sum(n):
#      if (n==1):
#           return 1
#      return sum(n-1) + n


# n = int(input("Enter the Value: "))
# print(f"The Sum is {sum(n)}")



#Q5

# def pattern(n):
#     if (n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# n = int(input("Enter the Value: "))
# pattern(n)


#Q6

# def inch_To_Cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))
# print(f"The corresponding value in cms is {inch_To_Cms(n)}")

#Q7

# def rem(list,word):
#     n = []
#     for item in list:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# list = ["aman","rohan","izx"]
# print(rem(list,"izx"))

#Q8

def multi_Table(n):
    for i in range (1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter Number: "))
multi_Table(n)