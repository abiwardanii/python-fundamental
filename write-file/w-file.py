food = open("food.txt", "w")
print(food.writable())
if food.writable():
    print("file dapat diisi")
else:
    print("file tidak dapat diisi")
print("============")

foods = open("food.txt", "r+")
print(foods.readable())
print(foods.writable())
if foods.writable() and foods.readable():
    print("file dapat ditulis dan dibaca")
else:
    print("file tidak dapat diisi dan dibaca")
print("=============")

name = open("nama.txt", "a") # append
name.write("\n haha")
name.close()

warna = open("warna.txt", "w")
warna.write("kuning")
warna.close()

car = open("car.txt", "w") #jika file tidak makan langsung akan dibuatkan
car.write("mobil")
car.close()

