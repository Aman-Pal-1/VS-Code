# 01_walrus operator( := ) is introduce in python 3.8 


# if (n := len([1,2,3,4,5,6]))>3:
#     print(f"The length is too long  ({n} five elements excepted <=3) ")


#  type definition
# # from typing import Union, List, Tuple, Dict  



# n : int = 5
# name : str = "Uditya"

# def sum(a:int,b:int)-> int:
#     return a+b

# a = int(input("Enter the Value of a :"))
# b = int(input("Enter the Value of b :"))

# c = sum(a,b)
# print(f"The value of a is {a} and value of b is {b} the sum of these are : {c}.")


# match case


# def https_status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 400:
#             return "good"
#         case 600:
#             return "Excellent"
#         case _:
#             return "Unknown Status"
        

# try:
#     user_input = int(input("Enter the https_status : "))
#     print(https_status(user_input))
# except ValueError:
#     print("Enter a valid Integer:")


# merge two dictionaries


# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'd':4}
# merged = dict1 | dict2
# print(merged)
  


# with open('fileuseinpythonIO.txt', 'r') as f1, open('prac9log.txt', 'w') as f2:
#     # Read content from the first file
#     content = f1.read()
    
#     # Process content (optional, for example, convert text to uppercase)
#     processed_content = content.upper()
    
#     # Write the processed content to the second file
#     f2.write(processed_content)

# print("Data processed and written successfully!")



# exception handling

# try:
#     a = int ( input ("Enter a number : "))
#     print(a)

# except Exception as e:
#     print(e)

# print("Thank You")

## try:
##     code
## except ZeroDivisionError :
##     code
## except TypeError :
##     code 
## except:
##    code 


# raising exception


# a = int (input( " enter the value of a :"))
# b = int (input( " enter the value of b :"))

# if (b == 0) :
#     raise ZeroDivisionError("Hay our program is not for any no. divisible by zero.")
# else:
#     print(f"The value of a/b is {a/b} .")


# try with else clause


# try: 
#     a = int (input( "hey, Enter any no. :"))
#     print(a)

# except Exception as e:
#     print(e)
# else:   # this is executed when the try was successfully Executed.
#     print("I am inside else.")  



# try with finallly clause



try: 
    a = int (input( "hey, Enter any no. :"))
    print(a)

except Exception as e:
    print(e)
finally:   # this is executed in the function also when we direct print in the function then it give error so we use finally. even if the function returns
    print("I am inside finally.")