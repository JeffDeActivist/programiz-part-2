# class SelfIterator:
#     def __iter__(self):
#         self.a = 3
#         return self
#
#     def __next__(self):
#         if self.a < 150:
#             x = self.a
#             self.a *= 2
#             return x
#         else:
#             raise StopIteration
#
#
# my_class = SelfIterator()
# Iter1 = iter(my_class)
# print(next(Iter1))
# print(next(Iter1))
# print(next(Iter1))
# print(next(Iter1))
#
# class Iter2:
#     def __init__(self, num):
#         self.num = num
#
#     def __iter__(self):
#         self.a = 0
#         return self
#
#     def __next__(self):
#         if self.a <= self.num:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#

#
#
# a = Iter2(10)
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)), print(next(i))
# print(next(i))
# another way to run it and will not have any limit...
# for i in Iter2(20):
#     if i % 2 == 0:
#         print(i)
# class Iter3:
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= self.limit:
#             x = self.a
#             self.a = self.a + 1
#             return x
#         else:
#             raise StopIteration
#
#
# # for i in Iter3(10):
# #     print(i)
# a = Iter3(10)
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
