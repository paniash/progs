# To generate the Fibonacci sequence
def fib(n):
    a = 0
    b = 1
    for i in range(0,n):
        print(b)
        temp = b
        b = temp + a
        a = temp

fib(100)

