#Tulis sebuah fungsi yang mengembalikan yang lebih kecil dari 
#dua angka yang diberikan jika kedua angka genap, 
#tetapi mengembalikan yang lebih besar jika satu atau kedua angka ganjil

def less_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print(f"angka genap terendah: {a}")
        else:
            print(f"angka genap terendah: {b}")
    elif a < b:
        print(f"angka terendah: {a}")
    else:
        print(f"angka terendah: {b}")
less_evens(2,6)