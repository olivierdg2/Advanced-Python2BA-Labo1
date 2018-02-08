# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import math

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(3),6)
        self.assertEqual(fact(1),1)
        self.assertEqual(fact(0),1)
        self.assertEqual(fact(5),120)

        pass
    
    def test_roots(self):
        sel.assertEqual(roots(1,1,1),)
        pass
    
    def test_integrate(self):

        pass

print(runner.run(suite))
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
