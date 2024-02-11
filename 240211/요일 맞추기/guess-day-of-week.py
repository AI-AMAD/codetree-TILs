m1, d1, m2, d2 = map(int, input().split())

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
minus_days = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]

count_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1d1 = 0
m2d2 = 0

for i in range(1, m1):
    m1d1 += count_days[i]
m1d1 += d1

for i in range(1, m2):
    m2d2 += count_days[i]
m2d2 += d2

if m2d2 > m1d1:
    distance_day = m2d2 - m1d1
    result = distance_day%7
    print(days[result])
else:
    distance_day = abs(m2d2 - m1d1)
    result = distance_day%7
    print(minus_days[result])