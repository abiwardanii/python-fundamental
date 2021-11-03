def check_string(mystring):
    up_case = 0
    low_case = 0
    sentence = mystring.replace(' ','')
    print(sentence)
    for item in sentence:
        if item.isupper() == True:
            up_case += 1
            # print(item)
        elif item.islower() == True:
            low_case += 1
            # print(item)
        else:
            pass
    return up_case, low_case
print(check_string('Halo Mas Abi, Bagaimana kabarmu di hari Minggu ini?')) 
