num = [1,2,3,4]
total = sum(num)
print(total)

maxNum = max(num)
print(maxNum)

num.sort()
max_num = num[-1]
print(max_num)

number = [4,5,1,9,10]
max_number = number[0]
for num in number:
    if num > max_number:
        max_number = num
print(max_number)