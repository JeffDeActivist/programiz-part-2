def gen():
    n = 0
    while n <= 20:
        yield n
        n += 2
        yield n
        n += 3

# for i in gen():
#     print(i)
a = gen()
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))