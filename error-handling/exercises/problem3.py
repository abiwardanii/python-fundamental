def input_num():
    try:
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        print("That's not a number!")
        return input_num()
input_num()
