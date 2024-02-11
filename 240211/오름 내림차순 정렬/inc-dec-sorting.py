n = int(input())
numbers = [i for i in map(int, input().split())]
numbers = sorted(numbers)
numberst = numbers[::-1]
print(numbers)
print(numberst)