def kantong_belanja(*args, **kwargs):
    print(args)
    print(kwargs)
    print('saya membeli {} {}'.format(args[1],kwargs['snack'])) #bisa diganti
kantong_belanja(2,4,6,buah='mangga',snack='potato',minuman='milo')