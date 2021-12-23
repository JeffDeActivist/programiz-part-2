"""simple multiplication table"""
for i in range(1, 11):
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)

"""adding natural numbers within a range"""
a = []
b = int(input("Enter a number\n"))
for i in range(b + 1):
    if b < 0:
        print(b, "is not a natural number")
    else:
        a.append(i)
# print("The sum is", sum(a))
"""find if a number is divisible by another"""
a = int(input("Enter number to be divided\n"))
b = int(input("Enter the divisor\n"))
if a % b == 0:
    print(a, "is completely divisible by", b, "and yields", a / b)
else:
    print(a, "is not completely divisible by", b)
"""ascii values of characters, chr() can be used to reverse"""
letters = ["A", 'a', 'b', 'c', 'd', 'e', 'p', ';', '9']
for i in letters:
    print(i, ":", ord(i))
"""factorials of a number"""
x = 32
for i in range(1, x+1):
    if x % i == 0:
        print(i, end=',')
vowels = 'a', 'e', 'i', 'o', 'u'
number = 1, 2, 3, 4, 5
name = ['jeff', 'www', 'https', 'ostrich', 'lion']
for i in vowels:
    print(i, end='\n')
for j in name:
    print(j, end='\n')
for i in name:
    for j in vowels:
        if j in i:
            print("'", j, "'", "Present in", i)

"""fun"""
add_count = 1
sub_count = 10
sign = '*'
while add_count <= 10:
    print('jeff', sign*add_count, "DeActivist", sign*sub_count)
    add_count += 1
    sub_count -= 1
