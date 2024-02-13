n = int(input())
OFF_SET = 1000
section = [0 for i in range(OFF_SET*2+2)]
standard = 0

elments = []

for i in range(n):
  distance, direction = input().split()
  distance = int(distance)
  if direction == "R":
    left_standard = standard
    right_standard = standard + distance
    standard += distance
    elments.append([left_standard, right_standard])
  else:
    left_standard = standard - distance
    right_standard = standard
    standard -= distance
    elments.append([left_standard, right_standard])

for x1, x2 in elments:
  x1 += OFF_SET
  x2 += OFF_SET
  for j in range(x1, x2):
    section[j] +=1

count=0
for sect in section:
  if sect >= 2:
    count +=1

print(count)