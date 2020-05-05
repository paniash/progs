# to sum of even terms of Fibonacci sequence
a = 1
b = 2
sum = 0
for i in range(5):
    a, b = b, a+b
    while a<4000000:
        if a%2==0:
            sum+=a

print("The sum is ", sum)


