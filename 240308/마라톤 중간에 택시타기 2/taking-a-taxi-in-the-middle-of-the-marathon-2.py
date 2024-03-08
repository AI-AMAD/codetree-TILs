import sys

n = int(input())

check_point = [
  tuple(map(int, input().split()))
  for _ in range(n)
]

distance = sys.maxsize

def taxi_distance(x1, x2, y1, y2):
  distance = abs(x1-x2) + abs(y1-y2)
  return distance


for i in range(1, n-1):
  slice_check_point = check_point[:i] + check_point[i+1:]
  temp = 0
  for j in range(1, len(slice_check_point)):
    x2, y2 = slice_check_point[j]
    x1, y1 = slice_check_point[j-1]
    temp += taxi_distance(x1, x2, y1, y2)
  distance = min(temp, distance)

print(distance)