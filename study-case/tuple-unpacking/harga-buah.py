fruits = [('apel',100),('pisang',200),('mangga',300)]

def harga_buah(fruits):
    harga_sekarang = 0
    nama_buah = ''
    for nama,harga in fruits:
        if harga > harga_sekarang:
            harga_sekarang = harga
            nama_buah = nama
    return(nama_buah,harga_sekarang)
#cara 1
hasil = harga_buah(fruits)
print(hasil)
print(type(hasil))
print('\n')
#cara 2
name,price = harga_buah(fruits)
print(name)
print(price)
print(type(name))
print(type(price))