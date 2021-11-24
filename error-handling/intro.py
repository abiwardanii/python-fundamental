try:
    # num = 2 + '2' output pasti error karena string tidak bisa dijumlahkan dengan int
    num = 2 + 2
except:
    # block code ini akan di eksekusi jika terjadi error
    print('An error occurred!')
else:
    # block code ini akan di eksekusi jika tidak terjadi error
    print('No error occurred!')
    print(num)
finally:
    # block code ini akan di eksekusi kapanpun(error atau tidak)
    print('This will always be executed!')
