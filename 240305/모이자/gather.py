import sys

n = int(input())
numbers = list(map(int, input().split()))
result = sys.maxsize

for i in range(1, n+1):
  temp = 0
  for idx, number in enumerate(numbers, start=1):
    if i != idx:
      temp += number * abs(idx-i)
    else:
      temp += number * 0
  result = min(result, temp)

print(result)