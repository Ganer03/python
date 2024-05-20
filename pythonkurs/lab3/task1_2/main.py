import math


def ccw(A, B, C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def is_point_inside_polygon(p, polygon):
    def sign(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    n = len(polygon)
    inside = False

    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        if (a.y <= p.y < b.y or b.y <= p.y < a.y) and p.x < a.x + (b.x - a.x) * (p.y - a.y) / (b.y - a.y):
            inside = not inside

    return inside



class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def move(self, dx, dy):
        self.a.move(dx, dy)
        self.b.move(dx, dy)
        self.c.move(dx, dy)

    def area(self):
        return 0.5 * abs((self.a.x - self.c.x) * (self.b.y - self.a.y) - (self.a.x - self.b.x) * (self.c.y - self.a.y))

    @staticmethod
    def compare(t1, t2):
        return abs(t1.area() - t2.area())

    @staticmethod
    def is_intersect(t1, t2):
        points1 = [t1.a, t1.b, t1.c]
        points2 = [t2.a, t2.b, t2.c]
        for i in range(0, 3):
            for j in range(0, 3):
                if i+1 == 3:
                    k = 0
                else:
                    k = i + 1

                if 1+j == 3:
                    l = 0
                else:
                    l = j + 1
                if intersect(points1[i], points1[k], points2[j], points2[l]):
                    return True
        return False

    @staticmethod
    def is_include(t1, t2):
        points1 = [t1.a, t1.b, t1.c]
        points2 = [t2.a, t2.b, t2.c]

        for i in range(3):
            if not is_point_inside_polygon(points1[i], points2):
                return False
        return True


class Pentagon:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def move(self, dx, dy):
        self.a.move(dx, dy)
        self.b.move(dx, dy)
        self.c.move(dx, dy)
        self.d.move(dx, dy)
        self.e.move(dx, dy)

    def area(self):
        side_length = math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)
        return 1.25 * side_length ** 2 / math.tan(math.pi / 5)

    @staticmethod
    def compare(p1, p2):
        return abs(p1.area() - p2.area())

    @staticmethod
    def is_intersect(p1, p2):
        points1 = [p1.a, p1.b, p1.c, p1.d, p1.e]
        points2 = [p2.a, p2.b, p2.c, p2.d, p2.e]

        for i in range(5):
            for j in range(5):
                if i + 1 == 5:
                    k = 0
                else:
                    k = i + 1

                if 1 + j == 5:
                    l = 0
                else:
                    l = j + 1
                if intersect(points1[i], points1[k], points2[j], points2[l]):
                    return True
        return False

    @staticmethod
    def is_include(p1, p2):
        points1 = [p1.a, p1.b, p1.c, p1.d, p1.e]
        points2 = [p2.a, p2.b, p2.c, p2.d, p2.e]

        for i in range(5):
            if not is_point_inside_polygon(points1[i], points2):
                return False
        return True


# create points
p1 = Point(1, 1)
p2 = Point(2, 3)
p3 = Point(3, 2)

p4 = Point(0, 0)
p5 = Point(6, 0)
p6 = Point(2, 4)

# create triangle
triangle = Triangle(p1, p2, p3)
triangle1 = Triangle(p4, p5, p6)
# move triangle
print('Intersect:')
print(triangle.is_intersect(triangle, triangle1))
print('Includes:')
print(triangle.is_include(triangle, triangle1))
triangle.move(-2, -2)
print("Area of triangle:", triangle.area())
print("Area of triangle:", triangle1.area())
print("Comparison by area:", triangle.compare(triangle, triangle1))

p11 = Point(-1, -1)
p22 = Point(0, 3)
p33 = Point(2, 4)

p44 = Point(5, 3)
p55 = Point(3, -1)
p56 = Point(7, -1)

# create pentagon
pentagon = Pentagon(p1, p4, p2, p3, p5)
pentagon1 = Pentagon(p11, p22, p33, p44, p55)
pentagon2 = Pentagon(p11, p22, p33, p44, p56)
print('Intersect:')
print(pentagon.is_intersect(pentagon, pentagon1))
print(pentagon.is_intersect(pentagon, pentagon2))
print('Includes:')
print(pentagon.is_include(pentagon, pentagon1))
print(pentagon.is_include(pentagon, pentagon2))

# move pentagon
pentagon.move(-1, 0)

# calculate area of pentagon
print("Area of pentagon:", pentagon.area())
print("Area of pentagon:", pentagon2.area())

# compare triangle and pentagon by area
print("Comparison by area:", Triangle.compare(pentagon, pentagon1))
