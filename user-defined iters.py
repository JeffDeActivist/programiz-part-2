class EvenNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# b = EvenNumbers()
# c = iter(b)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))  # raises StopIteration
for c in EvenNumbers():
    if c % 2 == 0:
        print(c, "is an even number",)
