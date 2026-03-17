from proekt640 import funk320FIO
from proekt640QOBILOV import funcQOBILOV

if __name__ == "__main__":
    choice = input("1 - сложение, 2 - функция: ")

    if choice == "1":
        print(funk320FIO(int(input("a: ")), int(input("b: "))))
    elif choice == "2":
        funcQOBILOV(int(input("число: ")))
######
from funk_kuchkarova import tg_x

x = float(input("Введите угол: "))

result = tg_x(x)

print("tg(", x, ") =", result)