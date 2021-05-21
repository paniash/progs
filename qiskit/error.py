p1 = 0.01
p3 = 3 * p1**2 * (1-p1) + p1**3
# p3 = p1**3 + 3*p1**2
print('Probability of a single reply being garbled: {}'.format(p1))
print('Probability of a the majority of three replies being garbled: {:.4f}'.format(p3))
