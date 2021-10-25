def myfunc(*args):
    print(args) #output tuples
    for item in args:
        print(item)
# *args = tuple parameter

myfunc(2,4,5,1)