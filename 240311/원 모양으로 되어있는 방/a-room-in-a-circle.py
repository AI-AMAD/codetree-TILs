import sys

n = int(input())
room = [ 
  int(input())
  for _ in range(n)
]

result = sys.maxsize
temp = 0

def change_room(c_room):
  c_room.append(c_room.pop(0))
  return c_room

for _ in range(n):
  room = change_room(room)
  for i, j in zip(room, range(n)):
    temp += i*j
  result = min(result, temp)

print(result)