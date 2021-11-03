#cara1
def uniq(num):
    uniq_list = []
    for n in num:
        if n not in uniq_list:
            uniq_list.append(n)
    print(uniq_list)
uniq([1,1,1,1,3,3,3,2,2,2,2,4,4,4])
print('\n')

#cara2
def uniq2(num):
    return list(set(num))
print(uniq2([1,1,1,1,3,3,3,2,2,2,2,4,4,4]))