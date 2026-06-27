# test_chainway.py
"""
Tests for ChainWay module.
"""

import unittest
from chainway import ChainWay

class TestChainWay(unittest.TestCase):
    """Test cases for ChainWay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainWay()
        self.assertIsInstance(instance, ChainWay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainWay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
