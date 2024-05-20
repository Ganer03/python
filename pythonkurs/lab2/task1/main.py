def main():
    filename = "input.txt"
    language = {}
    maxer = 0
    b = []
    with open(filename, 'r') as file:
        n = int(file.readline())
        for i in range(0,n):
            lister = file.readline().strip('\n')
            if lister.isdigit():
                j = int(lister)
                i += j+1
                c = []
                for k in range(0,j):
                    lister = file.readline().strip('\n')
                    if lister in language:
                        language[lister] += 1
                    else:
                        language[lister] = 1
                    c.append(lister)
                if j>maxer:
                    maxer = j
                    b = c
    count = 0
    lister = []
    print(language)
    for i in language:
        if language[i] == n:
            lister.append(i)
            count += 1
    print(count)
    for i in range(len(lister)):
        print(lister[i])
    print(maxer)
    b.sort()
    for i in b:
        print(i)


if __name__ == "__main__":
    a = {}
    main()