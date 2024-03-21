import sys, copy

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

result = sys.maxsize

def two_except_list_sum(index_1, index_2):
  number_list = copy.deepcopy(numbers)
  number_list[index_1] = 0
  number_list[index_2] = 0
  sum_list = sum(number_list)
  return sum_list
  

for i in range(n):
  for j in range(i+1, n):
    sum_number = two_except_list_sum(i, j)
    temp = abs(s-sum_number)
    result = min(result, temp)

print(result)