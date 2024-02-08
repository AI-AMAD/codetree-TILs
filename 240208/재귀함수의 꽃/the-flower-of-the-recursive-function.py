n = int(input())

def print_count(n):
    if n == 0:
        return
    print(n, end=' ')
    print_count(n-1)
    print(n, end=' ')

print_count(n)