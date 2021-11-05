def user_input():
    range_inputs = range(1, 10) # range(1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    in_range = False # in_range = False
    choise = 'wrong' # choise = 'wrong'

    #perulangan akan berhenti jika user menginputkan angka!
    while choise.isdigit() == False or in_range == False:
        choise = input('Inputkan angka 1 sampai 9: ')

        #cek apakah input berupa angka atau tidak
        if choise.isdigit() == False:
            print('inputkan angka!')
        
        if choise.isdigit() ==  True:
            if int(choise) in range_inputs:
                in_range = True
            else:
                pass
    print(int(choise))

user_input()