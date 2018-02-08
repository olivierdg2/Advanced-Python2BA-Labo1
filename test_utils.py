# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import math

class TestUtils(unittest.TestCase):
    def test_fact(self):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)
        pass
    
    def test_roots(self):
        delta = b^2 - (4*a*c)
        if delta > 0
            root1 = (b + sqrt(delta))/(2*a)
            root2 = (b - sqrt(delta))/(2*a)
            return (root1,root2)
        if delta = 0
            root = (b/(2*a))
            return (root)
        else
            return()
        pass
    
    def test_integrate(self):

        pass

print(runner.run(suite))
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
