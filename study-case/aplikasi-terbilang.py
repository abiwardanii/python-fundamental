nums = input("Masukan angka: ")

num_map = {
    "1" : "satu",
    "2" : "dua",
    "3" : "tiga",
    "4" : "empat",
    "5" : "lima",
    "6" : "enam",
    "7" : "tujuh",
    "8" : "delapan",
    "9" : "sembilan"
}
output = ""
for n in nums:
    counted = num_map.get(n, "invalid")
    output = output + counted + " "
print(output)