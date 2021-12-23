""" manually iterating over a list"""
l1 = [1, 34, 45, 'jeff', 'ken', 'samantha']
l2 = iter(l1)
print("memory location of the iterator object", l2).
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
# print(next(l2))  # raises StopIteration

"""automatically iterating over a list"""
l3 = iter(l1)
for a in l3:
    print('for iteration:', a)
