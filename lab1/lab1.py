import matplotlib.pyplot as mt
import numpy as np


# a) Pentru functia f:[0,4] -> R f(x) = x^3 - 7x^2 + 14x - 6, desenati graficul functiei

# functia
def f(x):
    return x ** 3 - 7 * (x ** 2) + 14 * x - 6


start = 0
stop = 4
val = 1000

dom = np.linspace(start, stop, val)
mt.plot(dom, f(dom))
mt.ylabel('Y')
mt.xlabel('X')
mt.show()

# b) Pentru intervalele [(0, 1), (1, 3.2), (3.2, 4)] si precizia eps = 10e-5, calculati
# numarul de pasi si solutiile ecuatiei f(x) = 0

vals = [(0, 1), (1, 3.2), (3.2, 4)]
eps = 10 ** (-5)
sol = []


def solve(start, stop, eps=10e-10):
    N = 0
    m = (start + stop) / 2
    while abs(f(m)) > eps:
        if f(start) * f(m) < 0:
            stop = m
        else:
            start = m
        N += 1
        m = (start + stop) / 2

    return N, m

# afiseaza rezultatele
for (start, stop) in vals:
    (N, m) = solve(start, stop, eps)
    sol.append((N, m))
    print(start, stop, N, m)

# c) pentru fiecare subinterval, deseneaza graficul si solutia
for i in range(len(sol)):
    dom = np.linspace(vals[i][0], vals[i][1], val)
    mt.plot(dom, f(dom))
    mt.plot(sol[i][1], f(sol[i][1]), 'g*')
    mt.ylabel('Y')
    mt.xlabel('X')
    mt.show()

# pentru functia f, deseneaza toate solutiile
dom = np.linspace(0, 4, val)
mt.plot(dom, f(dom))
for i in range(len(sol)):
    mt.plot(sol[i][1], f(sol[i][1]), 'g*')
mt.show()
