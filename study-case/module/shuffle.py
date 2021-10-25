from random import shuffle
mylist = [' ','0',' ']

def shuffle_list(list_num):
    shuffle(list_num)
    return list_num

def user_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("pilih angka 0,1,2: ")

    return int(guess)
user_guess()

def check_guess(list_num,guess):
    if list_num[guess] == '0':
        print("Benar")
        print(list_num)
    else:
        print("Salah")
        print(list_num)

mix_list = shuffle_list(mylist)
guess = user_guess()
check_guess(mix_list,guess)
