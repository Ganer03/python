from math import ceil


def main(filename):
    with open(filename, 'r') as f:
        n = f.readline().split()
        r = int(n[0])
        t = int(n[1])
        elems = []
        rightSum = 0
        leftSum = 0
        for i in range(0, r):
            a, b = map(int, f.readline().split())
            elems.append([a, ceil(b / t)])
        cost = [0] * r
        elems.sort()
        for i in range(1, r):
            cost[0] += abs(elems[i][0] - elems[0][0]) * elems[i][1]
            rightSum += elems[i][1]
        for i in range(1, r):
            leftSum += elems[i - 1][1]
            cost[i] = abs(cost[i - 1] - rightSum * (elems[i][0] - elems[i - 1][0]) + leftSum * (
                        elems[i][0] - elems[i - 1][0]))
            rightSum -= elems[i][1]
        print(min(cost))


if __name__ == "__main__":
    a = {}
    main("27-122a.txt")
    main("27-122b.txt")
