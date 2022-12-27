#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:  6782 -> 23           0,56 -> 11 
number = input("Введите вещественное число: ")
summa=0
for i in number:
    if i.isdigit():
        summa+=int(i)
print(summa)





"""def InputNumbers(inputText):
    yes = False
    while not yes:
        try:
            number = float(input(f"{inputText}"))
            yes = True
        except ValueError:
            print("Пожалуйста, введите цифры")
    return number

num = InputNumbers("Введите число: ")

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum



print(f"Сумма цифр = {sumNums(num)}")"""