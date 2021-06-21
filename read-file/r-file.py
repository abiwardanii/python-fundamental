greeting = open("greeting.txt", "r")
print(greeting.read())
print("========")
greeting.close()

halo = open("halo.txt", "r")
str = (halo.readlines())
print(str[0])
print(str[1])
print(str[2])
halo.close()

hari = open("hari.txt", "r")
array = hari.readlines()
index = 1
for h in array:
    print(f"{index} - {h}")
    index += 1
hari.close()

color = open("warna.txt", "r")
print(color.readable())
if color.readable():
    print("file dapat dibaca")
else:
    print("file tidak dapat baca")
color.close()

# w = write
# r = membaca
# a = menambah