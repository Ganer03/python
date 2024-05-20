month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
def date(b):
    b = b.split()
    for i in range(0, len(b)-2):
        if b[i].isdigit() and b[i+2].isdigit():
            if int(b[i])>0 and int(b[i])<32  and b[i+1] in month and int(b[i+2])>1924 and int(b[i+2])<2025:
                print(b[i] + ' ' + b[i+1] + ' ' + b[i+2])


a = input('Введите строку с датами: ')
date(a)