n = list(input())
end = len(n)
result = 0

for i in range(1, end):
  if n[i] == '(' and n[i-1] == '(':
    for j in range(1, end):
      if n[j] == ')' and n[j-1] == ')':
        result += 1

print(result)