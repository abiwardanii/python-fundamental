#Diberikan tiga bilangan bulat antara 1 dan 11, 
# jika jumlahnya kurang dari atau sama dengan 21, kembalikan jumlah mereka. 
# Jika jumlahnya melebihi 21 dan ada sebelas, kurangi jumlah totalnya dengan 10. 
# Terakhir, jika jumlahnya (bahkan setelah penyesuaian) melebihi 21, kembalikan 'LOSE'
def blackjack(*args):
    num = sum(args)
    if num <= 21:
        print(num)
    elif num > 21 and 11 in args:
        print(num - 10)
    else:
        print('LOSE')
blackjack(1,2,3)


