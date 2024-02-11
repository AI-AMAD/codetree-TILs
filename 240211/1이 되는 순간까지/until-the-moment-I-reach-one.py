n = int(input())
count = 0
def nanugi(n):
    global count
    if n == 1:
        return count
    if n%2==0:
        count += 1
        n //= 2
        return nanugi(n)
    else:
        count += 1
        n //= 3
        return nanugi(n)

count = nanugi(n)
print(count)