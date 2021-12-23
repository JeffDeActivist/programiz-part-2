"""iter expression"""

# a = [12, 23, 34, 55, 64, 45, 24]
# b = iter(a)
# print(b.__next__())
# print(b.__next__() * 2, "is a calculated value")
# """Generator expression"""
# c = (i ** 2 for i in range(10))
#
# print(next(c))
# for i in [x**2 for x in range(10)]:
#     if i % 2 == 0:
#         print(i, "is divisible by 2")
#     else:
#         print(i, "is not divisible by 2")
#
# """set comprehension"""
# w = [x**2 for x in range(10)]
# y = {x**2 for x in range(10)}
# print("w is an ordered list of", w)
# print("y is an unordered  set of", y)
# q = 'Jeff'
# q1 = (q.upper() for i in q)
# print(q1.__next__())
# """generator expression"""
# u = sum(1 for x in range(1000) if x % 2 == 0 and '9' in str(x))
# print(u)
