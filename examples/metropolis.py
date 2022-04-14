import freevirgil

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
HC = [0] * irange
MS = [0] * irange

for i in range(0, irange):

    T[i] = 0.1 * (i + 1)
    E[i], M[i], EE[i], MM[i] = mcarlo.metropolis(ham, spin, T[i])
    HC = (EE[i] - E[i]*E[i]) / (T[i]*T[i])
    MS = (MM[i] - M[i]*M[i]) / T[i]

plt.figure(num = 0, dpi = 100)
plt.plot(T, E, label="<E>")
plt.plot(T, M, label="<M>")
plt.plot(T, HC,  label="HC")
plt.plot(T, MS, label="MS")
plt.legend()
plt.xlabel("Temperature")

plt.savefig("metropolis.png")
