d = {'a1':1, 'a2':2, 'a3':3}

for item in d:
    print(item)
#hanya key saja yg tercetak
for item in d.items():
    print(item)
#semua tercetak
for key,value in d.items():
    print(value)
#value tercetak cara 1
for value in d.values():
    print(value)
#value tercetak cara 2