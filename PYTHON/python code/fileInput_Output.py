'''
a = "a very long string with emails"
emails = []
3 seconds
'''

# file.read 

f = open("fileuseinpythonIO.txt")
data = f.read()
print(data)
f.close()

# file.write

st = "Aman bhai is very cool guy."

f = open("fileuseinpythonIO2.txt","w")
f.write(st)
f.close()

# file.read lines

f = open("fileuseinpythonIO.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()

# file.readline

f = open("fileuseinpythonIO.txt")
line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))
line = f.readline()
while(line !=""):
     print(line)
     line = f.readline()

f.close()

# file.append

st = "Aman bhai to hacker nikle amazing.\n"
f = open("fileuseinpythonIO.txt","a")
f.write(st)
f.close()

# file_with

# The same can be written using with statement like this :

with open("fileuseinpythonIO.txt") as f:
     print(f.read())

# You dont have to explicitly close the file.