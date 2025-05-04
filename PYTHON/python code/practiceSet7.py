#q1

# table = int(input("Enter the no. for printing table :"))
# i = 1
# for i in range(1,11):
#     print(f"{table} X {i} = {i*table}")

#q2

# l = ["Harry","Soham","Sachin","Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(name)

#q3

# table = int(input("Enter the no. for printing table :"))

# i = 1

# while(i<11):
#     print(f"{table} X {i} = {table*i}")
#     i+=1

#q4

# num = int(input("Enter the number:"))

# for i in range(2, num):
#     if(num%i) == 0:
#         print(num," is not prime")
#         break
# else:
#     print(num," is prime.")  

#q5

# num = int(input("Enter the number:"))
# i = 1
# sum = 0
# while (i<=num):
#     sum += i
#     i+=1

# print(sum)

#q6

# n = int(input("Enter no. :"))

# product = 1
# for i in range(1,n+1):
#     product = product*i
# print(f"The Factorial of {n} is {product}")

#q7

'''
for n = 3

  *
 ***
*****

'''

# n = int(input("Enter the number:"))

# for i in range (1,n+1):
#     print(" "*(n-i),end = "")
#     print("*"*(2*i-1),end="")
#     print(" ")

#q8

# n = int(input("Enter the number:"))

# for i in range (1,n+1):
#     print("*"*i,end="")
#     print("")


#q9

# n = int(input("Enter the number:"))

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end = "")
#     else:
#         print("*",end = "")
#         print(" "*(n-2), end = "")
#         print("*",end = "")
#     print("")

#q10

table = int(input("Enter the no. for printing table :"))

for i in range(1,11):
    print(f"{table} X {11-i} = {table*(11-i)}")
