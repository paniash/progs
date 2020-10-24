def f(x):
    return x**2 - 1

def bisection(a, b, tol):
    xl = a
    xr = b
    while (abs(xl-xr) >= tol):
        c = (xl+xr)/2.0
        prod = f(xl)*f(c)
        if prod > tol:
            xl = c
        elif prod < tol:
            xr = c

    return c

answer = bisection(0, 3, 1e-8)
print("Num:", answer)
