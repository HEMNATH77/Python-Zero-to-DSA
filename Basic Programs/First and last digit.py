def first(n):
    while n >=10:
        n = n // 10
    return n
def last(n):
    return  n % 10

n= int(input("enter no : "))
print(first(n),end=" ")
print(last(n))