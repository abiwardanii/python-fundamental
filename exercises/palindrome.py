# cara1
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
print('\n')
#cara2
def palindrome2(s):
    s = s.replace(' ', '')

    if s == s[::-1]:
        print(True)
    else:
        print(False)
palindrome2('halo hai')
palindrome2('kasur rusak')
palindrome2('nurse run')