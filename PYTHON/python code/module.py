def myFunc():
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    return a + b

if __name__ =="__main__":
    # if this code is directly executed by running the file its present in .
    print("we are directly running this code")

c = myFunc()
print(f"The Addition of a and b is : {c} .")

print(__name__)
