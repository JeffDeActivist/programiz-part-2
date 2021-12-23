# is a simple way of creating iterators
# a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""t is fairly simple to create a generator in Python. It is as easy as defining a normal function with
yield statement instead of a return statement. If a function contains at least one yield
statement (it may contain other yield or return statements), it becomes a generator function.
Both yield and return will return some value from a function. The difference is that, while a
return statement terminates a function entirely, yield statement pauses the function saving all
its states and later continues from there on successive calls. Here is how a generator function
differs from a normal function.
 Generator function contains one or more yield statement.
 When called, it returns an object (iterator) but does not start execution immediately.
 Methods like __iter__() and __next__() are implemented automatically. So we can iterate
through the items using next().
 Once the function yields, the function is paused and the control is transferred to the caller.
 Local variables and theirs states are remembered between successive calls.
 Finally, when the function terminates, StopIteration is raised automatically on further calls."""


# def my_yield():
#     n = 2
#     yield n
#     n = n * 2
#     yield n
#     n = n * 3
#     yield n
#     n = n - 2
#     yield n
#     n = n * 3
#     yield n


""" to access values"""
# a = my_yield()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
"""can be iterated over using a for loop"""
# for a in my_yield():
#     print(a)
#
# """generator expressions are created by using () and list expressions use []"""
# """The major difference between a list comprehension and a generator expression is that while list
# comprehension produces the entire list, generator expression produces one item at a time. They
# are kind of lazy, producing items only when asked for. For this reason, a generator expression is
# much more memory efficient than an equivalent list comprehension."""
# a = [1, 2, 5, 7, 5, 12, 45]
# list comprehension
# b = [i**2 for i in a]
# f = sum([i**2 for i in a])
# print(b)  # returns whole list
# generator expression
# c = (i**2 for i in a)
# e = sum((i**2 for i in a))
# print(c)  # returns memory location
# print(e)
# print(f)
# # to access value sof a generator expression
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))  # raises StopIteration
# """why generators are used"""
# # easy to implement
# # represent infinite stream
# # memory efficient
"""to restart the iteration ou just need to create another generator object"""

# a = my_yield()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
"""yields all even numbers"""

# def ally():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
#
# a = ally()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

"""generator to print numbers divisible by 3"""

# def div_two():
#     n = 0
#     while True:
#         yield n
#         n += 3
# a = div_two()
# print(next(a))
# print(next(a))
# print(next(a))
# def ab():
#     for x in range(234, 260):
#         yield x ** 0.5
#
#
# a = ab()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a) + 2)  # the generator results can be used anywhere...this has been called from line 32 for instance
"""Notice that a generator's body is not immediately executed: when you call function() in the example above, it
immediately returns a generator object, without executing even the first print statement. This allows generators to
consume less memory than functions that return a list, and it allows creating generators that produce infinitely long
sequences.
GoalKicker.com – Python® Notes for Professionals 348
For this reason, generators are often used in data science, and other contexts involving large amounts of data.
Another advantage is that other code can immediately use the values yielded by a generator, without waiting for
the complete sequence to be produced.
"""
