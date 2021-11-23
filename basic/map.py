def square_num(num):
    return num ** 2
mynum = [1,2,3,4]
for num in map(square_num,mynum):
    print(num)

print(list(map(square_num,mynum)))
print('\n')

def mynames(name):
    if len(name) % 2 == 0:
        return 'genap'
    else:
        return name[0]
names = ['abi', 'togar','rexy', 'xian']
for item in map(mynames,names):
    print(item)
print(list(map(mynames,names)))