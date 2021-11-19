def binary_search(data, dicari):
    data.sort()
    awal = 0
    akhir = len(data) - 1
    mid = 0
 
    while awal <= akhir:
 
        mid = (awal + akhir) // 2
 
        # jika nilai dicari lebih besar, abaikan element disebelah kirinya
        if data[mid] < dicari:
            awal = mid + 1

        # jika nilai dicari lebih kecil, abaikan element disebelah kanannya
        elif data[mid] > dicari:
            akhir = mid - 1
 
        # angka yang dicari bereda di index tengah
        else:
            return mid
 
    # jika tidak ditemukan, kembalikan nilai -1
    return -1
 
 
# data array yang akan dicari
data = [ 13,67,78,1,2,6,45,87,54 ]
dicari = int(input ("Masukkan angka yang ingin dicari :"))
 
# Function call
hasil = binary_search(data, dicari)
 
if hasil != -1:
    print("Angka berhasil ditemukan pada index ke: ", str(hasil))
else:
    print("Angka tidak berhasil ditemukan")