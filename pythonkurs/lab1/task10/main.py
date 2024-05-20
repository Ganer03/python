# Задание 10 Дан список строк с клавиатуры. Упорядочить по количеству
# слов в строке.

def stroke(a):
    a.sort(key=lambda x: len(x.split(' ')))
    print(a)


str = []
a = input('Введите строку: ')
while a != '0':
    str.append(a)
    a = input('Введите строку: ')

print('Упорядоченный список:')
stroke(str)