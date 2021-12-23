# def my_name(names):
#     def name1():
#         print(names)
#
#     name1()
#
#
# my_name("jeff")
# """closure form of above"""
#
#
# def my_name(names):
#     def name1():
#         print(names)
#
#     return name1()
#
#
# a = my_name("jeff")
# print(a)
# """That's unusual. The print_msg() function was called with the string "Hello" and the returned
# function was bound to the name another. On calling another(), the message was still
# remembered although we had already finished executing the print_msg() function. This
# technique by which some data ("Hello") gets attached to the code is called closure in Python.
# """
# del my_name
# print(a)
# my_name("jeff2")
def mul(x):
    print("step 1")

    def mu(n):
        print("step 2:", x * n)
        return x * n

    return mu


a = mul(2)
print(a(2))
print(mul(2)(12))
