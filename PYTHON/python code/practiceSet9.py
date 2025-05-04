#Q1

# f = open("practice9poem.txt")
# data = f.read().lower()
# word = input("Guess a word is in poem :").lower()
# if(word in data):
#     print("The word Twinkle is in the content .")
# else:
#     print("The word Twinkle is not in the content .")
# print(data)
# f.close()



#Q2

# import random

# def game():
#     print("You are playing the game.")
#     score = random.randint(1,62)
#     with open("practice9q2.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"your Score {score}")
#     if(score>hiscore):
#         with open("practice9q2.txt","w") as f:
#             f.write(str(score))

#     return score

# game ()



#Q3

# def gen_Table(n):
#     table=""
#     for i in range (1,11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"table/practice{n}.txt","w") as f:
#         f.write(table)
#     # return table

# for i in range(2,21):
#     gen_Table(i)



#Q4

# word = "donkey"

# with open("practiceset9q4.txt") as f:
#     content = f.read()

# contentNew = content.replace(word,"#####")

# with open("practiceset9q4.txt","w") as f :
#     f.write(contentNew)


#Q5

# words = ["Donkey","Douglas","than"]

# with open("practiceset9q4.txt","r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word,"#" * len(word))

# with open("practiceset9q4.txt","w") as f :
#     f.write(content)




#Q6

# with open("prac9log.txt") as f:
#     content = f.read()
# if ("python" in content ):
#     print("Yes python is present.")
# else:
#     print("Noo python is not present.")




#Q7

# with open("prac9log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines :
#     if "python" in line.lower():
#         print(f"Yes python is present in line {lineno}.")
#         break
#     lineno += 1

# else:
#     print("Noo python is not present.")



#Q8

# with open("prac9q8this.txt","r") as f:
#     content =f.read()

# with open("prac9q8this2.txt","w") as f:
#     f.write(content)




#Q9 
 
# with open("prac9q9f1.txt") as f :
#     content1 = f.read()
# with open("prac9q9f2.txt") as f :
#     content2 = f.read()

# if (content1 == content2) :
#     print("File1 and File2 data is same .")
# else:
#     print("File1 and File2 Data is Different.")


#Q10

# with open("prac9q10.txt","w") as f:
#     f.write("")



#Q11

with open("prac9q11file1.txt","r") as f:
    content = f.read()

with open("prac9q11file2.txt","w") as f:
    f.write(content)
