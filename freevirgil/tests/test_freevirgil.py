"""
Unit and regression test for the freevirgil package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import freevirgil
import numpy as np


def test_freevirgil_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "freevirgil" in sys.modules

def test_ham_energy():
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
        
if __name__== "__main__":
        test_freevirgil_imported()
        test_ham_energy()
