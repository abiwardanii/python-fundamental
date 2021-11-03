import string
#cara1
def pangram(str, alpha=string.ascii_lowercase):
    return set(alpha) <= set(str.lower())
print(pangram('The quick brown fox jumps over the lazy dog')) 

#cara2
def ispangram(str, alpha=string.ascii_lowercase):
    alpaset = set(alpha)
    str = str.replace(' ','').lower()
    str = set(str)
    return alpaset == str
print(ispangram('The quick brown fox jumps over the lazy dog'))

