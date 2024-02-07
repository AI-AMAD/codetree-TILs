n = int(input())

def a(n):
    if n == 0:
        return
    a(n-1)
    print(n, end=' ')

def b(n):
    if n == 0:
        return
    print(n, end=' ')
    b(n-1)


a(n)
print()
b(n)