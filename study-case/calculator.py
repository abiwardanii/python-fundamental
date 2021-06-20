command = ""

while command != "exit":
    command = input("Operasi: ")

    if command == "exit":
        break
    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Operasi tidak dikenali")
        continue
    a = int(input("input angka pertama: "))
    b = int(input("input angka kedua: "))

    if command == "+":
        hasil = a + b
    elif command == "-":
        hasil = a - b
    elif command == "*":
        hasil = a * b
    elif command == "/":
        hasil = a / b 
    print(f"Hasil: {hasil}")
print("Aplikasi Dihentikan")