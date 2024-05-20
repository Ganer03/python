# Задание 9 Прочитать список строк с клавиатуры. Упорядочить по длине
# строки.
def stroke(a):
    a.sort(key=lambda x: len(x))
    print(a)


str = []
a = input('Введите строку: ')
while a != '0':
    str.append(a)
    a = input('Введите строку: ')

print('Упорядоченный список:')
stroke(str)