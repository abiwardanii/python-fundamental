import csv

name = open("name.csv", "r")

name_csv = csv.reader(name, delimiter=",") #delimiter = pemisalah antar kolom
print(name_csv)

for row in name_csv:
    print(row) #tipe list/array
    print(f"nama: {row[0]}, posisi:{row[1]}, umur:{row[2]}")

name.close()