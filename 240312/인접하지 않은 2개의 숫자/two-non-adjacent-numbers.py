import sys
n = int(input())
numbers = list(map(int, input().split()))

result = -sys.maxsize
temp = 0

for i in range(n):
  for j in range(n):
    if j == i or abs(j-i) == 1:
      continue
    else:
      temp += numbers[i] + numbers[j]
    result = max(result, temp)
    temp = 0

print(result)