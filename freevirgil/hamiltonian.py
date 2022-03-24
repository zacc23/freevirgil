import math
from matplotlib import pyplot as plt

class hamiltonian():
    
    def __init__(self, N=10, J=-2.0, mu=1.0, k=1.0):
        
        self.N = N
        self.J = J
        self.mu = mu
        self.k = k
    
    def E(self, spin):
    
        sites = len(spin)
        
        sum1 = 0
        sum2 = 0
        for i in range(0, sites-1):
            sum1 += spin[i] * spin[i+1]
            sum2 += spin[i]
            if (i == sites-2):
                sum1 += spin[i+1] * spin[0]
                sum2 += spin[i+1]
           
        return (-self.J * sum1) + (self.mu * sum2)      

    def M(self, spin):
        """
        note: Magnetization does not need Hamiltonian constants (mu, J)
        TODO: separate into Config class
        """
        sites = len(spin);
        
        N_up = 0
        N_down = 0
        for i in range(0, sites):
            if spin[i] == 1:
                N_up += 1
            else:
                N_down += 1
        
        return N_up - N_down
    
    def avg(self, conf, T):
        
        Z = 0.0
        E = 0.0
        M = 0.0
        EE = 0.0
        MM = 0.0
        
        configs = conf.dim
        spin = [0] * configs

        for i in range(0, configs):
                    
            # generate each possible configuration
            spin = conf.dec_conf(i)
            #print(spin)
            
            Ei = self.E(spin)
            Zi = math.exp( -Ei/(self.k*T) )
            E += Ei * Zi
            EE += Ei * Ei * Zi
            
            Mi = self.M(spin)
            M += Mi * Zi
            MM += Mi * Mi * Zi
            Z += Zi
              
        E = E/Z
        M = M/Z
        EE = EE/Z
        MM = MM/Z

        heat_capacity = (EE - E*E) / (self.k*T*T)
        magnetic_susceptibility = (MM - M*M) / (self.k*T)

        return E, M, heat_capacity, magnetic_susceptibility 
