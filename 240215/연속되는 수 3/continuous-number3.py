n = int(input())
numbers = [int(input()) for _ in range(n)]

max_continuity = 0
temp = 0

def plus_minus_check(number):
  if number > 0:
    return True
  elif number < 0:
    return False

for i in range(n):
  if i == 0 or plus_minus_check(numbers[i]) == plus_minus_check(numbers[i-1]):
    temp += 1
    max_continuity = max(max_continuity, temp)
  elif plus_minus_check(numbers[i]) != plus_minus_check(numbers[i-1]):
    max_continuity = max(max_continuity, temp)
    temp = 1

print(max_continuity)