def power(n,x):
    p = 1
    for i in range(1,x+1):
        p = p * n
    return p

n = 8
x = 2
print(power(n,x))


