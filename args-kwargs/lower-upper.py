def myfunc(x):
    result = []
    for i in range(len(x)):
        if i%2==0:
            result.append(x[i].lower())
        else:
            result.append(x[i].upper())
    print(result)
    print(''.join(result))
    return ''.join(result)
myfunc('asdfgdnvduvasjhjmknoij')