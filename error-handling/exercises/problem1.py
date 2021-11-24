try:
    for i in ['a', 'b', '' ]:
        print(i**2)
except TypeError:
    print('Unsupported operator')
