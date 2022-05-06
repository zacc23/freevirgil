"""
Unit and regression test for the hamiltonian class.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import freevirgil

def test_energy():
        spin = freevirgil.spin_conf(N=2)
        ham = freevirgil.hamiltonian(J=-2, mu=1.1)
        spin.dec_conf(2)
        
        assert(ham.E(spin) == -4.0)
        
def test_avg_energy():

        spin = freevirgil.spin_conf(N=2)
        ham = freevirgil.hamiltonian(J=-2, mu=1.1)

        E, M, HC, MS = ham.avg(spin, 1)
        
        # E ~= -3.99104425
        assert(-3.9910443 < E < -3.9910442)
        # M ~= -0.00298581
        assert(-0.0029859 < M < -0.0029858)
        # HC ~= 0.05269599
        assert(0.0526959 < HC < 0.0526960)
        # MS ~= 0.00611116
        assert(0.0061111 < MS < 0.0061112)
        
if __name__ == "__main__":
        test_energy()
        test_ham_energy()
