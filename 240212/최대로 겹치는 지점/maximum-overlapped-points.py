n = int(input())
numbers = [0 for i in range(n+1)]

for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2+1):
        numbers[j]+=1
max_ = max(numbers)
print(max_)