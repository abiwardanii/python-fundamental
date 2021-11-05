game_list = [0,1,2]
def display_game(game_list):
    print("Daftar yang tersedia: ")
    print(game_list)
# display_game(game_list)

def position_choice():
    choise = 'wrong'
    while choise not in ['0','1','2']:
        choise = input("Masukkan posisi yang ingin dituju(0,1,2): ")
        if choise not in ['0','1','2']:
            print("Posisi tidak tersedia")
    return int(choise)
# position_choice()

def replacement(game_list, position):
    user_placement = input("Inputkan string pada posisi tersebut: ")
    game_list[position] = user_placement
    return game_list
    # print(game_list)
# replacement(game_list,1)

def games_choise():
    choise = 'wrong'
    while choise not in ['Y', 'N']:
        choise = input("Tetap bermain(Y or N): ")
        if choise not in ['Y', 'N']:
            print("Input tidak valid, pilih Y / N")
    if choise == 'Y':
        return True
    else:
        return False
# games_choise()

game_on = True
game_list = [0,1,2]
while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement(game_list,position)

    display_game(game_list)

    game_on = games_choise()
