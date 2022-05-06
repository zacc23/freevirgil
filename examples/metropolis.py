import freevirgil
import matplotlib.pyplot as plt

# spin configuration
spin = freevirgil.spin_conf(N=2)
# ising hamiltonian
ham = freevirgil.hamiltonian(J=-2, mu=1.1)
# montecarlo metropolis
mcarlo = freevirgil.montecarlo(n_sweep=1000, n_burn=100, T=1)

irange = 100
T = [0] * irange
E = [0] * irange
M = [0] * irange
EE = [0] * irange
MM = [0] * irange
EvT = [0] * irange
MvT = [0] * irange
HCvT = [0] * irange
MSvT= [0] * irange

for i in range(0, irange):

    T[i] = 0.1 * (i + 1) + 1

    E, M, EE, MM = mcarlo.metropolis(ham, spin, T[i])   

    EvT[i] = E[-1]
    MvT[i] = M[-1]
    HCvT[i] = (EE[-1] - E[-1]*E[-1]) / (T[i]*T[i])
    MSvT[i] = (MM[-1] - M[-1]*M[-1]) / T[i]
    print(EvT[i], MvT[i], HCvT[i], MSvT[i])

plt.figure(num = 0, dpi = 100)
plt.plot(T, EvT, label="<E>")
plt.plot(T, MvT, label="<M>")
plt.plot(T, HCvT,  label="HC")
plt.plot(T, MSvT, label="MS")
plt.legend()
plt.xlabel("Temperature")

plt.savefig("metropolis.png")
