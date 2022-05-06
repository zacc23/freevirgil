"""
Unit and regression test for the spin_conf class.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import freevirgil
import numpy as np

def test_spin_conf():

        spin = freevirgil.spin_conf(N=2)

        assert(spin.sites == 2)
        assert(spin.dim == 4)

        assert(spin.config[0] == 0)
        assert(spin.config[1] == 0)

def test_magnetization():

        spin = freevirgil.spin_conf(N=2)
        print(spin.M())
        assert(spin.M() == -2)

def test_dec_conf():

        spin = freevirgil.spin_conf(N=2)        
        # 1, 0 -> 1, -1
        spin.dec_conf(2) 
        conf = spin.config

        assert(conf[0] == 1)
        assert(conf[1] == -1)
        
if __name__ == "__main__":
        test_spin_conf()
        test_magnetization()
        test_dec_conf()
