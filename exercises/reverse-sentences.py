# Diberikan sebuah kalimat, kembalikan kalimat dengan kata-kata terbalik
def reverse_str(text):
    x = text.split()
    x = x[::-1]
    x = " ".join(x)
    print(x)
reverse_str('saya bangun pagi')