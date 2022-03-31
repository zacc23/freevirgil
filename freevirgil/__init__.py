"""
FreeVirgil
Introduction to the Free Virgil method
"""

# Add imports here
from .freevirgil import *
from .hamiltonian import *
from .spin_conf import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
