# Given an integer n, return True if n is within 10 of either 100 or 200
def check_num(num):
    if 10 < num < 100 or 10 < num < 200:
        print(True)
    else:
        print(False)
check_num(209)