n = int(input())
white = 0
black = 0
gray = 0
standard = 100000
checked = [0]*(200001)
white_checked = [0]*(200001)
black_checked = [0]*(200001)

for i in range(n):
  distance, direction = input().split()
  distance = int(distance)
  if direction == "R":
    while distance > 0:
      checked[standard] = 2
      black_checked[standard] += 1
      distance -= 1
      if distance:
        standard +=1
  else:
    while distance > 0:
      checked[standard] = 1
      white_checked[standard] += 1
      distance -= 1
      if distance:
        standard -= 1
for i in range(0, len(checked)):
  if white_checked[i] >= 2 and black_checked[i] >= 2:
    gray += 1
  elif checked[i] == 1:
    white += 1
  elif checked[i] == 2:
    black += 1

print(white, black, gray)