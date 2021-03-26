"""
QUBEKit GUI
A GUI for the QUBEKit software.
"""

# Add imports here
from .gui import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
