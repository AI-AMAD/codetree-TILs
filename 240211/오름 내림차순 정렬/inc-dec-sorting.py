n = int(input())
numbers = [i for i in map(int, input().split())]
numbers = sorted(numbers)
numberst = numbers[::-1]

for i in numbers:
    print(i, end=' ')

print()

for j in numberst:
    print(j, end=' ')