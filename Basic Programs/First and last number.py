def first(n):
    while n >= 10:
        n = n/10
    return int(n)
def last(n):
    return (n % 10)

n = 75623
print(first(n),end = " ")
print(last(n))
