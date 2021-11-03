#cara 1
def check_string(str):
    up_case = 0
    low_case = 0
    for char in str:
        if char.isupper():
            up_case += 1
        elif char.islower():
            low_case += 1
        else:
            pass
    print(f'input string {str}')
    print(f'jumlah uppercase = {up_case}')
    print(f'jumlah lowercase =  {low_case}')
check_string('Halo Mas Abi, Bagaimana kabarmu di hari Minggu ini?')

print('\n')

#cara 2
def check_string2(str):
    d = {'up_case': 0, 'low_case': 0}
    for char in str:
        if char.isupper():
            d['up_case'] += 1
        elif char.islower():
            d['low_case'] += 1
        else:
            pass
    print(f'input string {str}')
    print(f'jumlah uppercase = {d["up_case"]}')
    print(f'jumlah lowercase =  {d["low_case"]}')
check_string2('Halo Mas Abi, Bagaimana kabarmu di hari Minggu ini?')