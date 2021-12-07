import random
print(random.randint(1, 10))

print('\n')

# value random akan selalu sama karna seed
random.seed(20)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print('\n')

mylist = list(range(1, 11))
print(random.choice(mylist))