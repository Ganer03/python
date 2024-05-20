import random
#3 Дана строка в которой слова записаны через пробел. Необходимо
# перемешать все слова этой строки в случайном порядке.
def peremesh(a):
    a = a.split()
    for i in range(len(a)):
        c = random.randint(0,len(a)-1)
        a[i], a[c] = a[c], a[i]
    b = ''
    for i in range(len(a)):
        b += a[i] + " "
    return b


# 8 Дана строка в которой записаны слова через пробел. Необходимо
# посчитать количество слов с четным количеством символов.
def kol(a):
    kol = 0
    a = a.split()
    for i in range(len(a)):
        if len(a[i]) % 2 == 0:
            kol += 1
    return kol


# 16 Дан массив в котором находятся строки "белый", "синий" и
# "красный" в случайном порядке. Необходимо упорядочить массив так, чтобы
# получился российский флаг.
def flag(a):
    color_values = {'белый': 0, 'синий': 1, 'красный': 2}
    sorted_arr = sorted(a, key=lambda x: color_values[x])
    return sorted_arr

print('Введите строку для задачи 1:')
a = input()
print('Перемешанная строка: ' + peremesh(a))

print('Введите строку для задачи 2:')
a = input()
print('Kol-vo: ', kol(a))


a = ["белый", "синий", "красный"]
for i in range(len(a)):
    c = random.randint(0, len(a)-1)
    a[i], a[c] = a[c], a[i]
print(a)
print('Строка для задачи 3: ', flag(a))