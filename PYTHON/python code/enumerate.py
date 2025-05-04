l = [1,2,3,4,5,6,7,8]

# index = 0
# for item in l:
#     index += 1
#     print(f"The item no. at index {index} is {item}")

# this can be simplified by enumerate function

for index, item in enumerate(l):
    print(f"The item no. at index {index} is {item}")