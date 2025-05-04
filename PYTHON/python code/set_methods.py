s = {1, 5,32,5,3,5,78,5,89,5,"Aman"} # set me elements repeat nii hote.
print(s,type(s))

s.add(566)
print(s,type(s))

s.remove(566)
print(s)

set = s.copy()
print(set)


set1 = {1,3,5}
set2 = {5,6,7}
print(set1.difference(set2))

set1.difference_update(set2)
print(set1)



s.discard(3)
print(s)

s.clear()
print(s)
