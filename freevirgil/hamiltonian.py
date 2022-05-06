import math

class hamiltonian():
    """
    Class for Hamiltonian
    
    .. math::
        H = -J\\sum_{\\left<ij\\right>} \\sigma_i\\sigma_j + \\mu\\sum_i\\sigma_i
    """

    
    def __init__(self, J=-2.0, mu=1.0):
        """
        Constructor

        Parameters
        ----------
        J : float, optional
            Coupling strength
        mu : float, optional
            Chemical potential
        """
        self.J = J
        self.mu = mu
    
    def E(self, spin):
        """
        Energy of configuration `spin`

        .. math::
                E = \\left<\\hat{H}\\right> 

        Parameters
        ----------
        spin : :class:`spin_conf`
            Spin configuration

        Returns
        -------
        energy : float
            Energy of configuration
        """
        sum1 = 0
        sum2 = 0
        for i in range(0, spin.sites-1):

            sum1 += spin.config[i] * spin.config[i+1]
            sum2 += spin.config[i]
            # Periodic boundary conditions
            if (i == spin.sites-2):
                sum1 += spin.config[i+1] * spin.config[0]
                sum2 += spin.config[i+1]
           
        return (-self.J * sum1) + (self.mu * sum2)      

    def avg(self, conf, T):
        """
        Exact average values

        Parameters
        ----------
        spin : :class:`spin_conf`
            Spin configuration
        T : int
            Temperature
        
        Returns 
        -------
        E : float
            Energy of configuration 
        M : float
            Magnetization of configuration
        HC : float
            Heat capacity
        MS : float
            Magnetic susceptability
        """     
         
        Z = 0.0
        E = 0.0
        M = 0.0
        EE = 0.0
        MM = 0.0
        
        for i in range(0, conf.dim):
                    
            # generate each possible configuration
            conf.dec_conf(i)
            
            Ei = self.E(conf)
            Zi = math.exp( -Ei/(T) )
            E += Ei * Zi
            EE += Ei * Ei * Zi
            
            Mi = conf.M()
            M += Mi * Zi
            MM += Mi * Mi * Zi
            Z += Zi
            print(Ei,Zi,E,EE,Mi,M,MM,Z) 
              
        E = E/Z
        M = M/Z
        EE = EE/Z
        MM = MM/Z

        heat_capacity = (EE - E*E) / (T*T)
        magnetic_susceptibility = (MM - M*M) / T

        return E, M, heat_capacity, magnetic_susceptibility 
