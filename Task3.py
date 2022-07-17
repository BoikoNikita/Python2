#Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму


n = int (input('Введите число: '))
list = list(range(n+1))
removed = list.pop(0)
for i in range(len(list)):
    list[i]= (1+1/list[i])
print(list)
print('Сумма чисел последовательности:', sum(list))