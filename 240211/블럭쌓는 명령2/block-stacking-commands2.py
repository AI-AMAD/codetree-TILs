n, k = map(int, input().split())
block_numbers = [0 for _ in range(n+1)]

for i in range(k):
    a, b = map(int,input().split())
    for j in range(a, b+1):
        block_numbers[j] += 1
print(max(block_numbers))