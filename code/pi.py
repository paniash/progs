def almost_pi(N):
    pi = 0
    for k in range(N):
        pi += ((-1)**k)/(2*k+1)

    return 4*pi

print(almost_pi(10000))
