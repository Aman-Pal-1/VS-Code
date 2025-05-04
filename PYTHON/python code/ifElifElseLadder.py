a = int(input("Enter your Age : "))

# if elif else ladder

if(a>=18) :
    print("You are Adult.")

elif(a==0):
    print("You enter 0 which is not a Valid Age.")

elif(a<0):
    print("Invalid Age.")

else :
    print("You are Teenager.")

print("End of Program")