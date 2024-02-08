n = int(input())

def sum_recur(n):
    if n == 1:
        return 1
    return n+sum_recur(n-1)

print(sum_recur(n))