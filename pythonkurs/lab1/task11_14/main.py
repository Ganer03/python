# Для задачи 3,5
def stroke(a):
    set = {}
    for i in a:
        if i not in set:
            set[i] = 1
        else:
            set[i] += 1
    s = max(set, key=set.get)
    return s


def stroke1(a):
    set = {}
    for i in a:
        for j in i:
            if j not in set:
                set[j] = 1
            else:
                set[j] += 1
    return set


def find_in_all(s, c):
    count = 0
    for i in s:
        for j in i:
            if s[i][j] == c:
                count += 1
    return count

def find_all(a):
    count = 0
    for i in a:
        count += len(i)
    return count


def max_str(c, a):
    count = 0
    for i in a:
        if i==c:
            count+=1
    return count


# Для задачи 9
def duncin(a):
    r = -1
    d = 0
    for i in range(0,len(a)):
        if ord(a[i])>d:
            d = ord(a[i])
            r = i
    return d - abs(ord(a[-r-1])-d)


# Для задачи 11
def calculate_average_weight(string):
    weigh = 0
    for i in range(len(string) - 2):
        tr_weight = calculate_weigh(string[i:i+3])
        weigh += tr_weight
    average_weight = weigh / (len(string) - 2)
    return average_weight


def calculate_weigh(triplet):
    weight = 0
    for char in triplet:
        weight += ord(char)
    return weight


def calculate_deviation(string):
    first_weight = calculate_average_weight(string[0])
    current_string_weight = calculate_average_weight(string)
    deviation = (first_weight - current_string_weight)**2
    print(string, deviation)
    return deviation


def sort_strings(strings):
    print('Частоты для 11')
    sorted_strings = sorted(strings, key=calculate_deviation)
    return sorted_strings


# 3 В порядке увеличения разницы между частотой наиболее часто
# встречаемого символа в строке и частотой его появления в алфавите.
str = []
a = input('Введите строку: ')
while a != '0':
    str.append(a)
    a = input('Введите строку: ')
c = stroke1(str)
d = find_all(str)
str1 = str
print('Упорядоченный список(для 3):')
str.sort(key=lambda x: (max_str(stroke(x), x)/len(x) - c[stroke(x)]/d))
print(str)
print('Частоты списка:')
for i in range(0, len(str)):
    print((max_str(stroke(str[i]), str[i])/len(str[i]) - c[stroke(str[i])]/d))


# 5 В порядке увеличения частоты квадратичного отклонения
# встречаемости самого часто встречаемого в строке символа от частоты его
# встречаемости в текстах на этом алфавите.
print('Упорядоченный список(для 5):')
str.sort(key=lambda x: (max_str(stroke(x), x)/len(x) - (c[stroke(x)]/d))**2)
print(str)
print('Частоты списка:')
for i in range(0, len(str)):
    print((max_str(stroke(str[i]), str[i])/len(str[i]) - (c[stroke(str[i])]/d))**2)


# 9 В порядке увеличения квадратичного отклонения между наибольшим
# ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
# расположенных символов строки (относительно ее середины).
a = input('Введите строку(для 9): ')
str = []
while a != '0':
    str.append(a)
    a = input('Введите строку: ')
print('Упорядоченный список(для 9):')
str.sort(key=lambda x: (duncin(x))**2)
print(str)
print('Частоты списка:')
for i in range(0, len(str)):
    print((duncin(str[i]))**2)


# 11 В порядке квадратичного отклонения дисперсии максимального
# среднего веса ASCII-кода тройки символов в строке от максимального
# среднего веса ASCII-кода тройки символов в первой строке.
a = input('Введите строку(для 11): ')
str = []
while a != '0':
    str.append(a)
    a = input('Введите строку: ')
sorted_strings = sort_strings(str)
print('Упорядоченный список(для 11):')
print(sorted_strings)
