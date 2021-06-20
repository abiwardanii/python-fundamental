# Game Tebak Angka
trying = 0
secret_num = 5
limit = 3

while trying < limit:
    guess_num = input("masukan angka(1-9): ")
    guess_num = int(guess_num)

    if guess_num == secret_num:
        print("kamu berhasil menebak")
        break
    
    trying += 1