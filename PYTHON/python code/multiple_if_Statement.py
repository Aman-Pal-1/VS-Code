a = int(input("Enter your Age : "))


# If statement no. : 1
if(a%2 == 0):
    print(a," is even")
# End of If statement no. : 1


# If statement no. : 2
if(a>=18) :
    print("You are Adult.")

elif(a==0):
    print("You enter 0 which is not a Valid Age.")

elif(a<0):
    print("Invalid Age.")

else :
    print("You are Teenager.")
# End of If statement no. : 2

print("End of Program")