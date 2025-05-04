#Q1



# try:
#     with open('1.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open('2.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open('3.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("Thank You !!")



#Q2



# l =[ 1,2,3,4,5,6,7,8,9,10]
# for i,item in enumerate(l):
#     if i == 2 or i ==4 or i==6 :
#         print(item)



#Q3


# num = int(input("Enter a number which you want to print table:"))

# table = [num*i for i in range(1,11)]
# print(table)



#Q4


# try: 
#     a = int ( input("Enter a number : "))
#     b = int (input ("Enter second Number : "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infinite")



#Q5

# num = int(input("Enter a number which you want to print table: "))

# table = [num*i for i in range(1,11)]
# with open ("advancetables.txt","a") as f:
#    f.write(f"Table of {num} : {str(table)} + \n")
# print(table)




