# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list_1 = list()
list_2 = list()
for i in range(n):
    number = int(input(f'введите {i+1}е число первого множества: '))
    list_1.append(number)
for i in range(m):
    number = int(input(f'введите {i+1}е число второго множества: '))
    list_2.append(number)
list_1 = set(list_1)
list_2 = set(list_2)
list_3 = list(list_1.intersection(list_2))
for n1 in range(len(list_3)):
    for n2 in range(n1+1, len(list_3)):
        if list_3[n1] > list_3[n2]:
            list_3[n1], list_3[n2] = list_3[n2], list_3[n1]
print(f'Ответ: {list_3}')
