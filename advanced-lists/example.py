l = [1,2,3]

#append
l.append(4)
print(l)

#count
print(l.count(1))

#apped list
a = [5,6,7]
b  = [8,9,10]
a.append(b)
print(a)

#extend
c = [5,6,7]
d  = [8,9,10]
c.extend(d)
print(c)

#index
print(l.index(3))

#insert
l.insert(2,4)
l.insert(3,"inserted")
print(l)

#pop
l.pop()
l.pop(0)
print(l)


#remove
l.remove(3)
print(l)

#reverse
l.reverse()
print(l)

#sort
my_l = [2,6,5,7,10,1]
my_l.sort()
print(my_l)

