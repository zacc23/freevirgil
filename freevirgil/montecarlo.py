import random

class montecarlo():
    """
    Class for MonteCarlo
    """

    def __init__(self, n_sweep=1000, n_burn=100, T=1):
        """
        Constructor

        Parameters
        ----------
        n_sweep : int, optional
            Number of sweeps
        n_burn : int, optional
            Number to burn
        """
        self.n_sweep = n_sweep
        self.n_burn = n_burn

    def sweep(self, ham, spin):
        """
        Sweep through all sites to 
        create a new configuration

        Parameters
        ----------
        ham : :class:`hamiltonian`
            Ising Hamiltonian
        spin : :class:`spin_conf`
            Spin configuration
        T : int
            Temperature
    
        Returns
        -------
        spin : :class:`spin_conf`
            New spin configuration
        """
        for i in range(0, spin.N)
        
            # all sites to the right and left
            rside = (i+1) % spin.N
            lside = (i+1) % spin.N

            if (spin.config[lside] == spin.config[rside]):
                if (spin.config[lside] == spin.config[i]): 
                    net_E = 4 * ham.J
                else:
                    net_E = -4 * ham.J

        # TODO: explain how this works
        net_E += 2*ham.mu * (2*spin.config[i] - 1) 
        
        usable = true
        if (net_E > 0):
        
            rand = random.random()
            if (rand > math.exp( -net_E/T )):
                usable = false

        if (usable):

            if (spin.config[i] == -1):
                spin.config = 1;
            else:
                spin.config = -1;

        return spin

    def metropolis(self, ham, spin, T)
        """
        Metropolis sampling

        Parameters
        ----------
        ham : :class:`hamiltonian`
            Ising Hamiltonian
        spin : :class:`spin_conf`
            Spin configuration
        T : int
            Temperature

        Returns
        -------
        Es : float list
             Energy of sample
        Ms : float list
             Magnetization of sample
        EEs : float list
              Average energy of sample      
        MMs : float list
              Average magnetization of sample
	"""
        # samples
        Es = [0] * n_sweep
        Ms = [0] * n_sweep EEs = [0] * n_sweep
        MMs = [0] * n_sweep

        for site in range(0, n_burn):

            self.sweep(ham, spin, T)
            
        self.sweep(ham, spin, T)    
        Ei = ham.E(spin)
        Mi = spin.M()

        Es[0] = Ei
        Ms[0] = Mi
        MMs[0] = Mi * Mi
        EEs[0] = Ei * Ei

        for s in range(1, n_sweep):
        
            self.sweep(spin, T)
            Ei = ham.E(spin)
            Mi = spin.M()

            Es[s] = (Es[s - 1]*s + Ei) / (s + 1)
            EEs[s] = (EEs[s - 1]*s + Ei*Ei) / (s + 1)

            Ms[s] = (Ms[s - 1]*s + Mi) / (s + 1)
            MMs[s] = (MMs[s - 1]*s + Mi*Mi) / (s + 1)

        return Es, Ms, EEs, MMs
