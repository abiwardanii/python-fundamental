def greetings(name, lesson):
    print(f"hai {name} selamat pagi")
    print(f"silahkan belajar {lesson}")

print("start")
greetings("abi", "python") #positional argument
print("==========")
greetings("xian", "java")
print("==========")
greetings(lesson="go", name="rexy") #keyword argument
print("finish")