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
def proizv(a, b):
    proizved = 1
    if b == 0:
        for i in range(len(a)):
            if int(a[i])!=0:
                proizved = proizved * int(a[i])
    else:
        for i in range(len(a)):
            if int(a[i]) % 5 != 0:
                proizved = proizved * int(a[i])
    return proizved


# Функция 3 Найти НОД максимального нечетного непростого делителя
# числа и произведения цифр данного числа.
def nod(a):
    b = 0
    if int(a/2) % 2 == 0:
        c = int(a/2) + 1
    else:
        c = int(a/2)
    for i in range(c, 2, -2):
        if a % i == 0:
            flag = 0
            for j in range(2, int(i/2)):
                if i % j == 0:
                    flag = 1
                    break
            if flag:
                b = i
                break
    if b:
        a = proizv(str(a),0)
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
    else:
        a = 0
    return a


print('Введите число для функции 1')
a = int(input())
max = max_easy_del(a)
if max:
    print('max_del_prost: ', max)
else:
    print('max_del_prost: not')

print('Введите число для функции 2')
a = input()
if proizv(a,5) == 1:
    print('нет таких чисел')
else:
    print('proizv: ', proizv(a,5))

print('Введите число для функции 3')
a = int(input())
print('nod: ', nod(a))