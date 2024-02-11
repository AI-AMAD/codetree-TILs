m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = 0 
for i in range(1, m1+1):
    a += days[i]
a += d1

b = 0
for i in range(1, m2+1):
    b += days[i]
b += d2

if m1 == m2:
    a+=1

print(b-a)