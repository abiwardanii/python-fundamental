try:
    age = input("umur anda: ")
    age = int(age)
    print(age)
except ValueError: #specific error
    print("input harus bertipe integer")