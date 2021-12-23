class OperatorOverloading:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return OperatorOverloading(x, y)

    def __str__(self):
        return f"point x is {self.x} and y is {self.y} after addition"

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return f"point x is {x} and point y is {y} after subtraction"

    def __eq__(self, other):
        x = self.x == other.x
        y = self.y == other.y
        return f"{x, y}"


o1 = OperatorOverloading(2, -2)
o2 = OperatorOverloading(1, 1)
o3 = OperatorOverloading(1, 1)
o4 = OperatorOverloading(1, 1)
print(o2 - o1)
print(o1 + o2)
print(o3 == o4)
print(3 / 2)
print(3 // 2)  # true division
