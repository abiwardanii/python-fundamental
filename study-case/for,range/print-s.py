nameInput = input("masukan huruf depan: ")
names = 'abiwardani rexy pradika chisrtian paul kurniawan leonardo yogi leonardo suhartono thomas wijaya'

for name in names.split():
    if name[0] == nameInput:
        print(name)