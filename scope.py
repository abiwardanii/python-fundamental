#global
name = 'global variable'

def hai():
    #enclosing
    name = 'abi'
    
    def halo():
        #local
        name = 'local'
        print('halo '+name)
    halo()
hai()