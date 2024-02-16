n = int(input())
numbers = [int(input()) for _ in range(n)]

max_count = 0
temp = 0

for i in range(n):
  if i == 0 or numbers[i] > numbers[i-1]:
    temp += 1
    max_count = max(max_count, temp)
  else:
    max_count = max(max_count, temp)
    temp = 1

print(max_count)