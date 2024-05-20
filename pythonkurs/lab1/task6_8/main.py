# 3 Дана строка. Необходимо найти общее количество русских символов.
def kol(a):
    r = 0
    for i in range(0, len(a)):
        if 1040 <= ord(a[i]) <= 1102:
            r += 1
    return r


# 8 Дана строка. Необходимо найти все используемые в ней строчные
# символы латиницы.
def kol_eu(a):
    r = 0
    for i in range(0, len(a)):
        if 97 <= ord(a[i]) <= 122:
            r += 1
    return r


# 16 Дана строка. Необходимо найти минимальное из имеющихся в ней
# целых чисел.
def minimal(a):
    a = a.split(" ")
    min = 0
    for i in range(len(a)):
        if a[i].lstrip('-').isdigit():
            min = int(a[i])
            break
    for i in range(len(a)):
        if a[i].lstrip('-').isdigit():
            if int(a[i])<min:
                min = int(a[i])
    return min


a = input()
print('Кол-во русских символов: ', kol(a))

a = input()
print('Кол-во строчных символов латиницы: ', kol_eu(a))

a = input()
print('Минимальное целое число: ', minimal(a))
