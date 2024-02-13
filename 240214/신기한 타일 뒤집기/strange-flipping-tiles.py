n = int(input())
standard = 100000
checked_tiles = [0] * (standard*2+1)
white = 0
black = 0

for i in range(n):
  distance, direction = input().split()
  distance = int(distance)
  if direction == "R":
    while distance > 0:
      checked_tiles[standard] = 2
      distance -= 1
      if distance:
        standard += 1
  elif direction == "L":
    while distance > 0:
      checked_tiles[standard] = 1
      distance -= 1
      if distance:
        standard -= 1
  
for i in range(len(checked_tiles)):
  if checked_tiles[i] == 2:
    black += 1
  elif checked_tiles[i] == 1:
    white += 1

print(white, black)