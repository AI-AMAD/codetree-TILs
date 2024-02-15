n = int(input())
numbers = [int(input()) for _ in range(n)]

max_continuity = 0
temp = 0

for i in range(n):
  if i == 0 or numbers[i] == numbers[i-1]:
    temp += 1
    #max_continuity = max(max_continuity, temp)
  elif numbers[i] != numbers[i-1]:
    max_continuity = max(max_continuity, temp)
    temp = 1

print(max_continuity)