#q1

# a1 = int(input("Enter No. 1 : "))
# a2 = int(input("Enter No. 2 : "))
# a3 = int(input("Enter No. 3 : "))
# a4 = int(input("Enter No. 4 : "))

# if (a1 > a2 and a1 > a3 and a1 > a4) :
#     print("Greater number is a1 :", a1)
# elif (a2 > a1 and a2 > a3 and a2 > a4) :
#     print("Greater number is a2 :", a2)
# elif (a3 > a2 and a3 > a1 and a3 > a4) :
#     print("Greater number is a3 :", a3)
# elif (a4 > a2 and a4 > a3 and a4 > a1) :
#     print("Greater number is a4 :", a4)

#q2

# marks1 = int(input("Enter Marks1 : "))
# marks2 = int(input("Enter Marks2 : "))
# marks3 = int(input("Enter Marks3 : "))

# # Check for total percentage 
# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are Pass", total_percentage)

# else:
#     print("You are failed", total_percentage)

#q3

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment : ")

# if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")

#q4

# username = input("Enter the username: ")

# if(len(username)<10):
#     print("Your username contains less than 10 characters")
# else:
#     print("All is well!.Your username contains greater than or equal to 10 characters")

#q5

# list = ["aman","rohan","harry","satyam"]
# name = input("Enter your name: ")
# if(name in list):
#     print("Your name is in the list.", name)
# else:
#     print("Your name is not in the list.", name)

#q6

# Your_marks = int(input("Enter Your Marks : "))

# if ( Your_marks>=90 and Your_marks<=100 ) :
#      print("Ex", Your_marks)
# elif ( Your_marks>=80 and Your_marks<90 ) :
#      print("A", Your_marks)
# elif ( Your_marks>=70 and Your_marks<80 ) :
#      print("B", Your_marks)
# elif ( Your_marks>=60 and Your_marks<70 ) :
#      print("C", Your_marks)
# elif ( Your_marks>=50 and Your_marks<60 ) :
#      print("D", Your_marks)
# elif ( Your_marks>=0 and Your_marks<50 ) :
#      print("F", Your_marks)
# else:
#      print("not valid number.")
#q7

post = input("Enter the Post: ")

if("Aman".lower() in post.lower()):
     print("This post is Talking about Aman")
else :
     print("This post is not Talking about Aman")
