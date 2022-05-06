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
        
if __name__ == "__main__":
        test_freevirgil_imported()
