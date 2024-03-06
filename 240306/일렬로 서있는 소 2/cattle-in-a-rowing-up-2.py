n = int(input())
cow_list = list(map(int, input().split()))
result = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if i<j<k and cow_list[i]<=cow_list[j]<=cow_list[k]:
        result += 1

print(result)