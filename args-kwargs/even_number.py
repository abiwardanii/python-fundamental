def myfunc(*args):
    num = []
    for item in args:
        if item % 2 == 0:
            num.append(item)
        else:
            pass
    print(num)
myfunc(1,2,4,5)