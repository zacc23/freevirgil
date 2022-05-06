import math
import freevirgil as fv
from matplotlib import pyplot as plt

spin = fv.spin_conf(N=10)
ham = fv.hamiltonian(J=-2, mu=1.1)

irange = 100
T = [0] * irange
E = [0] * irange
M = [0] * irange
HC = [0] * irange
MS = [0] * irange

for i in range(0, irange):

    T[i] = 0.1 * (i + 1)
    E[i], M[i], HC[i], MS[i] = ham.avg(spin, T[i])
    
plt.figure(num = 0, dpi = 100)
plt.plot(T, E, label="<E>")
plt.plot(T, M, label="<M>")
plt.plot(T, HC,  label="HC")
plt.plot(T, MS, label="MS")
plt.legend()
plt.xlabel("Temperature")

plt.savefig("plot.png")
