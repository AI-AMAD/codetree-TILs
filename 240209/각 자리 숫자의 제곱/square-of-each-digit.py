numbers = list(map(int, input()))
n = len(numbers)
ans = 0
def result(k):
    global n
    global ans
    if k == n:
        return ans
    ans+=numbers[k]**2
    return result(k+1)

ans = result(0)
print(ans)