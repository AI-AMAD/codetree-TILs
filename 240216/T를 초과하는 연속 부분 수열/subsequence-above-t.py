n, t = map(int, input().split())
numbers = list(map(int, input().split()))

max_continuity = 0
temp = 0

for number in numbers:
  if number <= t:
    max_continuity = max(max_continuity, temp)
    temp = 0
  elif number > t:
    temp += 1
    max_continuity = max(max_continuity, temp)

print(max_continuity)