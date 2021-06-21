user = {
    "nama" : "abi",
    "umur" : 23,
    "kerja" : True
}
user["nama"] = "abiwardani" #mengubah nilai
user["is_married"] = False #menambahkan nilai
print(user)
print(user["nama"])
print(user.get("username"))
temp = user.get("username", "manggala")
print(temp)