num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
operation = input("Введите операция над числом(+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)


def calc():
    global num3
    if operation == "+":
        num3 = num1 + num2
    elif operation == "-":
        num3 = num1 + num2
    elif operation == "*":
        num3 = num1 * num2
    elif operation == "/" and num2 == 0:
        print("Деление на 0 невозможно")
        change_num2()
        return calc()
    elif operation == "/" and num2 != 0:
        num3 = num1 / num2
    else:
        change_operation()
        return calc()

    #voice = input("Результат вывести на экран или в тхт? Напишите 1 - Экран или 2 - Файл")
    #output()


def change_operation():
    global operation
    operation = input("Введите операция над числом(+, -, *, /): ")


def change_num2():
    global num2
    num2 = input("Введите число неравное 0: ")
    num2 = float(num2)


""""
def output():
   if voice == 1:
        print("Результат: ", num3)
    elif voice == 2:
        print()
    else:
        change_voice()
        return
"""

calc()

voice = input("Результат вывести на экран или в тхт? Напишите 1 - Экран или 2 - Файл \n", )
voice = int(voice)
if voice == 1:
    print("Результат: ", num3)
elif voice == 2:
    print("Запись выполнена!")
    with open("/Users/arsenikatsuba/Desktop/study/calca/output.txt", "w") as file:
        file.write(str(num3))
else:
    print("Ошибка")
#change_voice()
