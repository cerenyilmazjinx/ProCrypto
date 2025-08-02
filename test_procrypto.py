# test_procrypto.py
"""
Tests for ProCrypto module.
"""

import unittest
from procrypto import ProCrypto

class TestProCrypto(unittest.TestCase):
    """Test cases for ProCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProCrypto()
        self.assertIsInstance(instance, ProCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
