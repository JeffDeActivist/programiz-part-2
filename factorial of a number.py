def rec_fact(x):
    if x == 1:
        return 1
    else:
        return x * (rec_fact(x - 1))


n = int(input("enter a number:"))
if n >= 1:
    print(rec_fact(n))
