n = int(input())

def hello_world(n):
    if n == 0:
        return
    hello_world(n-1)
    print("HelloWorld")

hello_world(n)