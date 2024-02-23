n, m = map(int, input().split())
information = [
  tuple(input().split())
  for _ in range(n+m)
]

a_array = []
b_array = []
a_current = 0
b_current = 0
result = 0

for i, (count, direction) in enumerate(information, start=1):
  count = int(count)
  if i <= n:
    if direction == "R":
      for _ in range(count):
        a_current += 1
        a_array.append(a_current)
    elif direction == "L":
      for _ in range(count):
        a_current -= 1
        a_array.append(a_current)
  else:
    if direction == "R":
      for _ in range(count):
        b_current += 1
        b_array.append(b_current)
    elif direction == "L":
      for _ in range(count):
        b_current -= 1
        b_array.append(b_current)

length_difference = abs(len(a_array) - len(b_array))
for _ in range(length_difference):
  if len(a_array) > len(b_array):
    b_array.append(b_array[-1])
  else:
    a_array.append(a_array[-1])

for i, (a, b) in enumerate(zip(a_array, b_array)):
  if i > 0 and a == b:
    if a_array[i-1] != b_array[i-1]:
      result += 1

print(result)