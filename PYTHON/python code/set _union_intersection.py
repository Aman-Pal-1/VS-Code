set1 = {1,3,5}
set2 = {5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))


set = set1-set2
print(set)

print({1,3}.issubset(set1))

print(set1.issuperset({1,2}))

print(set1.pop())

set1.clear()
print(set1)