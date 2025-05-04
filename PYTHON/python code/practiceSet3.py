# a = input("Enter Your Name : ")
# print("good afternoon",a)
#      # or
# print(f"good afternoon {a}")

# q2

letter = '''Dear <|Name|>,
You are Selected!
<|Date|>'''

print(letter.replace("<|Name|>","Uditya Pal").replace("<|Date|>", "24 july 2025"))


#  Q3

name = "uditya is a  good  boy and  "
print(name.find("  "))


#q4

name = "uditya is a  good  boy and  "
print(name.replace("  "," "))
print(name)  #strings are immutable which means that you can not change them by running functions on them

#q5

letter = "Dear Uditya ,\n \t this is python is nice. \n Thanks!"
print(letter)