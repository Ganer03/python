def main():
    filename = "input.txt"
    language = {}
    abc = {}
    mistakes = 0
    with open(filename, 'r') as file:
        n = int(file.readline())
        for i in range(0, n):
            list = file.readline().strip('\n')
            language[list] = 0
            if list not in abc:
                abc[list.lower()] = 0
        list = file.readline()
        list = list.split()
        for i in range(len(list)):
            count = 0
            words = []
            for j in range(len(list[i])):
                if list[i][j].isupper():
                    count += 1
                    words.append(j)
            if count == 1:
                if list[i].lower() in abc:
                    if list[i] not in language:
                        mistakes += 1
            elif count > 1:
                flag = False
                for j in range(count):
                    list1 = list[i].lower()
                    list1 = list1.replace(list1[words[j]], list[words[j]])
                    if list1 in language:
                        flag = True
                        break
                if not flag:
                    mistakes += 1
            else:
                mistakes += 1
    print(mistakes)


if __name__ == "__main__":
    a = {}
    main()