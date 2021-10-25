# arbitary keyword

def buah(**kwargs):
    print(kwargs) #output dictionary
    if 'buah' in kwargs:
        print('saya suka buah {}'.format(kwargs['buah']))
    else:
        print('saya tidak menemukan buah')
buah(buah='mangga',sayur='tomat')