import math
from matplotlib import pyplot as plt

class spin_conf:
    """
    Class for generating spin configurations   
        of various dimensions
    """

    def __init__(self, N=10):
        """
        Initialize configuration

        Parameters
        ----------
        N : int, default: 10
            Amount of sites
        
        Returns
        -------
        """
        self.N = N
        self.dim = 2**N
    
    def dec_conf(self, dec):
        """
        Convert decimal to binary (-1, 1)
        spin configuration
        
        Parameters
        ----------
        dec : int
            Decimal number to convert to
            binary (0, 1) -> (-1, 1)

        Returns
        -------
        conf : int list
            Spin configuration list (-1, 1)
        """
        conf = [int(i) for i in bin(dec)[2:]]
        
        for i in range(0, len(conf)):
            if conf[i] == 0:
                conf[i] = -1
        
        while len(conf) < self.N:
            conf = [-1] + conf
            
        return conf
        
# ADD FUNCTION for specifying possible config size
#configs = 2 ** self.N
#spin = [0] * configs

# ADJUST CLASS INIT for hamiltonian
#ham = hamiltonian(N, J=-2.0, k=1.1)
