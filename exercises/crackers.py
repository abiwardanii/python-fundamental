# tulis fungsi mengambil string dua kata dan mengembalikan True jika kedua kata dimulai dengan huruf yang sama
def crackers(str):
     x = str.split()
     if x[0][0] == x[1][0]:
         print(True)
     else:
         print(False)
crackers("halo Hai")    