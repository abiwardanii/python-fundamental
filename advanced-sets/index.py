my_set = set()

#add
my_set.add(1)
my_set.add(2)
print(my_set)

#clear
my_set.clear()
print(my_set)

#copy
my_set = {1, 2, 3}
my_set_copy = my_set.copy()
print(my_set_copy)

#difference
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
print(my_set_copy.difference(my_set))

#difference_update
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set_copy.difference_update(my_set)
print(my_set_copy)

#discard
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

#intersection
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
print(my_set_copy.intersection(my_set))

#intersection_update
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set_copy.intersection_update(my_set)
print(my_set_copy)

#isdisjoint
my_set = {1, 2, 3}
my_set_copy = {4, 5, 6}
my_set1 = {1, 2, 4}

print(my_set.isdisjoint(my_set_copy))
print(my_set.isdisjoint(my_set1))

#issubset
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set1 = {1, 2, 4}
print(my_set.issubset(my_set_copy))
print(my_set.issubset(my_set1))

#issuperset
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set1 = {1, 2, 4}
print(my_set.issuperset(my_set_copy))
print(my_set.issuperset(my_set1))

#symmetric_difference
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set1 = {1, 2, 4}
print(my_set.symmetric_difference(my_set_copy))
print(my_set.symmetric_difference(my_set1))

#union
my_set = {1, 2, 3}
my_set_copy = {1, 2, 3, 4, 5}
my_set1 = {1, 2, 4}
print(my_set.union(my_set_copy))
print(my_set.union(my_set1))
