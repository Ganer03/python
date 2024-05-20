# zad1
# Функция 1 Найти максимальный простой делитель числа.
def max_easy_del(a):
    delitel = 0
    for i in range(2, int(a / 2)):
        if a % i == 0:
            delit = 0
            for j in range(2, i):
                if i % j == 0:
                    delit += 1
            if delit == 0:
                delitel = i
    return delitel


# Функция 2 Найти произведение цифр числа, не делящихся на 5
def proizv(a):
    proizved = 1
    tr = 0
    for i in range(len(a)):
        if int(a[i]) % 5 != 0:
            proizved = proizved * int(a[i])
    return proizved


print('Введите число для функции 1')
a = int(input())
max = max_easy_del(a)
if max:
    print('max_del_prost: ', max)
else:
    print('max_del_prost: not')

print('Введите число для функции 2')
a = input()
if proizv(a) == 1:
    print('нет таких чисел')
else:
    print('proizv: ', proizv(a))
