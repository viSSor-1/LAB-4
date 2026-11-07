
def conv():
    x = input("Введите целое неотрицательное десятичное число: ")
    if not x.isdigit():
        print("Ошибка")
        return

    num = int(x)
    print(f"Двоичная система: {bin(num)[2:]}")
    print(f"Восьмеричная система: {oct(num)[2:]}")
    print(f"Шестнадцатеричная система: {hex(num)[2:]}")

conv()