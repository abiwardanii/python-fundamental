def input_num():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("That's not a number!")
        finally:
            print("This is always printed!")
    return num
input_num()
