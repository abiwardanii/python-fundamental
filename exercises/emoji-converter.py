msg = input(">>> ")

emoji_mpa = {
    ":)" : "😁",
    ":v" : "🤣",
    ":(" : "😔"
}

words = msg.split(" ")
output = ""
for w in words:
    output = output + emoji_mpa.get(w, w) + " "
print(output)