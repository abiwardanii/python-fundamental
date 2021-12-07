from collections import Counter

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]

print(Counter(mylist))

mylist1 = [1,1,1,1,'a','a','a','b','b','b']

print(Counter(mylist1))

mystr = ('aaaaabbbbcccccdddddeeeeefffff')
str = Counter(mystr)
print(str)
print(str.most_common()) # print semua
print(str.most_common(2)) # print 2 yang paling banyak


kata = "berapa banyak kata kata yang terhitung dalam kalimat ini"
print(Counter(kata.split()))

