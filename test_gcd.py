import unittest
from gcd_calculator import gcd_iterative, gcd_recursive

class TestGCDCalculator(unittest.TestCase):
    
    def test_iterative_gcd(self):
        # Test standard, prime, and zero cases for the iterative function
        self.assertEqual(gcd_iterative(48, 18), 6)
        self.assertEqual(gcd_iterative(13, 7), 1)
        self.assertEqual(gcd_iterative(0, 5), 5)
        
    def test_recursive_gcd(self):
        # Test standard, prime, and zero cases for the recursive function
        self.assertEqual(gcd_recursive(48, 18), 6)
        self.assertEqual(gcd_recursive(13, 7), 1)
        self.assertEqual(gcd_recursive(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
