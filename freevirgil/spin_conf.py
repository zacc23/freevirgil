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
        self.sites = N
        self.dim = 2**N
        self.config = [0] * N
    
    def M(self):
        """
        Magnetization of configuration

        Parameters
        ----------

        Returns
        -------
        M : float
            magnetization
        """
        #TODO: make sure config is right size

        N_up = 0
        N_down = 0
        for i in range(0, self.sites):
            if self.config[i] == 1:
                N_up += 1
            else:
                N_down += 1

        return N_up - N_down

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
        """
        conf = [int(i) for i in bin(dec)[2:]]
        
        for i in range(0, len(conf)):
            if conf[i] == 0:
                conf[i] = -1
        
        while len(conf) < self.sites:
            conf = [-1] + conf
            
        self.config = conf

    def set_conf(self, conf):
        """
        Specify binary (-1, 1) 
        spin configuration
        
        Parameters
        ----------
        conf : int list
            Spin configuration list (-1, 1)

        Returns
        -------
        """
        self.config = conf       
