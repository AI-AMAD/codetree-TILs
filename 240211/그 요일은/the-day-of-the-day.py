m1, d1, m2, d2 = map(int, input().split())
day = input()
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_map = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
result = 0

m1d1 = 0
for i in range(1, m1):
  m1d1 += days[i]
m1d1+=d1

m2d2 = 0
for i in range(1, m2):
  m2d2 += days[i]
m2d2+=d2

count_day = m2d2-m1d1
result = count_day//7

remain = count_day%7

if days_map[day] <= remain:
  result +=1
  print(result)
else:
  print(result)