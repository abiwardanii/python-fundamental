def palindrome(mystring):

    reverse_string = mystring[::-1].lower()
    input_str = mystring.lower()

    # print(reverse_string)
    if input_str == reverse_string:
        print(True)
    else:
        print(False)
palindrome('halo hai')
palindrome('kasur rusak')
palindrome('Kasur Rusak')