mynum = [1,2,3,4]

print(list(map(lambda num: num ** 2,mynum)))
print(list(filter(lambda num: num ** 2,mynum)))

# dari regular function
# def square_num(num):
#   return num ** 2

# diubah menjadi lambda expressions
# lambda num: num ** 2