#Diberikan string, kembalikan string di mana untuk setiap karakter dalam aslinya ada 2 karakter
def multiple_string(text):
    j = ''
    for i in text:
        j += i*2
        # print(i*2)
    print(j)
multiple_string('hallo')