n = int(input())
result = []

def recur(n):
    if n == 1:
        result.append(n)
        return
    else:
        result.append(n%2)
        return recur(n//2)
recur(n)
for i in result[::-1]:
  print(i,end='')