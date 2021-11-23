#harus mereturn true or false
def check_num(num):
    return num % 2 == 0
nums = [1,2,3,4,5,6,7,8]
for n in filter(check_num,nums):
    print(n)
print(list(filter(check_num,nums)))