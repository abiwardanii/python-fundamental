# Diberikan daftar int, kembalikan True jika array berisi 2 di sebelah 2 di suatu tempat.
def check_44(num):
    for i in range(0, len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True

    return False
print(check_44([1,2,3,3])) 
print(check_44([1,2,3])) 