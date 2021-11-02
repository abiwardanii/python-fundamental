def check_num(num,low,high):
    if low >= high:
        print('param kedua harus lebih kecil dari param ketiga')
    elif low < num < high:
        print(f'{num}, terletak diantara {low} dan {high} ')
    else:
        print(False)
check_num(4,2,6)
check_num(1,2,3)
check_num(4,8,6)
