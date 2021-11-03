# cara-1
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

print('\n')

#cara-2
def check_num2(num,low,high):
    if num in range(low,high+1):
        print(f'{num}, terletak diantara {low} dan {high} ')
    else:
        print(False)
check_num2(4,2,6)
check_num2(1,2,3)
check_num2(4,8,6)
