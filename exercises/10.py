# Diberikan dua bilangan bulat, 
# kembalikan True jika jumlah bilangan bulat adalah 10 atau jika salah satu bilangan bulat adalah 20. 
# Jika tidak, kembalikan False

def sum_ten(a,b):
    x = a + b
    if a == 10:
        print(True, "a bernilai 10")
    elif x == 10:
        print(True, "jumlah bernilai 10")
    else:
        print(False, "jumlah tidak bernilai 10")
sum_ten(3,5)