n = int(input())
numbers = [0 for i in range(201)]

for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    for j in range(x1, x2):
        numbers[j] += 1

print(max(numbers))