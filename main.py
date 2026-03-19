from proekt640 import funk320FIO
from proekt640QOBILOV import funcQOBILOV
from proekt640Tursunov import most_frequent

if __name__ == "__main__":
    choice = input("1 - сложение, \n2 - функция \n3 - Tursunov \n \n")

    if choice == "1":
        print(funk320FIO(int(input("a: ")), int(input("b: "))))
    elif choice == "2":
        funcQOBILOV(int(input("число: ")))

    elif choice == "3":
        user_input = input("Введите числа: ")
        nums = [int(x) for x in user_input.split()]
                
        result = most_frequent(nums)
                
        if result is None:
            print("Недостаточно уникальных чисел")
        else:
            print("Самое частое число:", result)
        
######
from funk_kuchkarova import tg_x

x = float(input("Введите угол: "))

result = tg_x(x)

print("tg(", x, ") =", result)