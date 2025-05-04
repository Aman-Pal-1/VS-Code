marks = {
    "Uditya" : 100,
    "Aman" : 99,
    "Rohan" : 70,
    1 : "Rohit"
} 
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry": 99, "renuka": 79})
print(marks)


print(marks.get("Uditya")) #print none when item not in the dictionary 
print(marks["harry"]) # give error when item not in the dictionary 
new_marks = marks.copy()
print(new_marks)

value = marks.pop("harry")
print(value)
print(marks)

item = marks.popitem()
print(item)
print(marks)
print(len(marks))
