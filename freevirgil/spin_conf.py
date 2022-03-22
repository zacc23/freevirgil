import math
from matplotlib import pyplot as plt

class spin_config:
 	"""
	Class for generating spin configurations   
		of various dimensions
	"""

    N=10
        
    def dec_conf(self, dec):
    
        conf = [int(i) for i in bin(dec)[2:]]
        
        for i in range(0, len(conf)):
            if conf[i] == 0:
                conf[i] = -1
        
        while len(conf) < self.N:
            conf = [-1] + conf
            
        return conf
        
# ADD FUNCTION for specifying possible config size
configs = 2 ** self.N
spin = [0] * configs

# ADJUST CLASS INIT for hamiltonian
ham = hamiltonian(N, J=-2.0, k=1.1)
