#q1

words = {
    "madad" : "help",
    "khushi" : "happy",
    "dil" : "heart"
}
word = input("Enter the word you want meaning of : ")
print(words[word])


#q2

s = set()
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))

print(s)


#q3

s= set()
s.add(18)
s.add("18")
print(s)

#q4

s = set()
s.add(20)
s.add(20.0)
s.add("20") #length of s after these operations ?

print(s)
 
#q5
s = { } #this is dictionary not a set
print(type(s))

#q6

d = {}
name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

print(d)

#q7

d = {}
name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter lang:")
d.update({name: lang})

print(d)


#q8

#we enter two values same but keys are different then  nothing will happen

#q9
#the values later will be update
s = {8,7,"Aman",[1,2]}

