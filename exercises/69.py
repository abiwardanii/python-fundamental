def sum_69(arr):
    hasil = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                hasil += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return hasil
print(sum_69([1,2,4]))
print(sum_69([2,4,6,9]))
print(sum_69([4,5,6,7,8,9]))