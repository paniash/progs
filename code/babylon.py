def babylonian_sqrt(S):

    if S == 0:
        return 0

    err = 10**(-10)

    init_guess = 20
    xn = init_guess

    while (abs(xn**2 - S)/S) > err:
        next_guess = 1/2 * (xn + S/xn)
        xn = next_guess

    return xn

print(babylonian_sqrt(5))
