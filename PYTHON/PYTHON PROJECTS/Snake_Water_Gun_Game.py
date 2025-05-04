'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice([-1,0,1])

print("You Chose any one of them Snake = s, Water = w, Gun = g. \n")
youstr=input("Enter Your Choice: ").lower()

youDict = {"s": 1, "w":-1,"g":0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}

if youstr not in youDict:
    print("Invalid input! Please choose 's','w',or'g'.")
else:
    you = youDict[youstr]
    print(f"You Choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")
    
    if computer==you:
        print("Its Draw!!!")

    else:
        if (computer == -1 and you == 1):
            print("You Win!")
        elif(computer == -1 and you == 0):
            print("You Lose!")
        elif (computer == 1 and you == -1):
            print("You Lose!")
        elif(computer == 1 and you == 0):
            print("You Win!")
        elif (computer == 0 and you == 1):
            print("You Lose!")
        elif(computer == 0 and you == -1):
            print("You Win!")

'''
if (computer == -1 and you == 1):               (computer-you)= -2
            print("You Win!")
        elif(computer == -1 and you == 0):      (computer-you)= -1
            print("You Lose!")
        elif (computer == 1 and you == -1):     (computer-you)= 2
            print("You Lose!")
        elif(computer == 1 and you == 0):       (computer-you)= 1
            print("You Win!")
        elif (computer == 0 and you == 1):      (computer-you)= -1
            print("You Lose!")
        elif(computer == 0 and you == -1):      (computer-you)= 1
            print("You Win!")

                or
the below logic is written on the basis of the value of computer - you .
        if((computer-you)==-1 or (computer-you)==2):
            print("You Lose!")
        else:
        print("You Win!")

'''