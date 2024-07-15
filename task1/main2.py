
# 1
`python main.py`

if __name__ == "__main__":
    while True:
        num1, num2, operator = myinputs()
result = calc(num1, num2, operator)
save()

exit = input("Хочешь выйти или нет?")
if exit:
    return 0
else:
    continue

    1111111
pass



# 2 Сделать обработку ошибок

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

# 3 Проверку на валидность операции (проверить, существует ли операция с таким знаком)
operation = input("Введите операция над числом(+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)


# 4 бесконечный цикл
()

# 5 +1 оператор
def calc(num1, num2, operation):
    if operation == "+":
        num3 = num1 + num2
    elif operation == "-":
        num3 = num1 + num2
    elif operation == "*":
        num3 = num1 * num2

    # 6 добавить обработку ошибок с заменой с знаменателя (try, except) + бесконечный цикл
    elif operation == "/" and num2 == 0:
        print("Деление на 0 невозможно")
        change_num2()
        return calc()
    elif operation == "/" and num2 != 0:
        num3 = num1 / num2

    return num3

# 7 вынести в отдеьлную функицю
# voice = input("Результат вывести на экран или в тхт? Напишите 1 - Экран или 2 - Файл")
# output()


# 8 подумать нужна ли функция эта
def change_operation():
    global operation
    operation = input("Введите операция над числом(+, -, *, /): ")

# 9 подумать нужна ли функция эта

def change_num2():
    num2 = input("Введите число неравное 0: ")
    num2 = float(num2)
    return num2


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

# 10 отдельная функиция
def save():
    voice = input("Результат вывести на экран или в тхт? Напишите 1 - Экран или 2 - Файл \n", )
    voice = int(voice)
    if voice == 1:
        print("Результат: ", num3)
    elif voice == 2:
        print("Запись выполнена!")
        with open("/task1/output.txt", "w") as file:
            file.write(str(num3))
    else:
        print("Ошибка")
    # change_voice()

save()
save()







