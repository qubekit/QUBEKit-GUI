"""
Unit and regression test for the qubekit_gui package.
"""

# Import package, test suite, and other packages as needed
import qubekit_gui
import pytest
import sys

def test_qubekit_gui_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "qubekit_gui" in sys.modules
