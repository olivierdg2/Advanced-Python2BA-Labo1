# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math
def fact(n):
         if n == 0:
            return 1
         else:
            return n*fact(n - 1)
        pass
def roots(a, b, c):
    delta = b^2 - (4*a*c)
        if delta > 0:
            root1 = (b + sqrt(delta))/(2*a)
            root2 = (b - sqrt(delta))/(2*a)
            return (root1,root2)
        if delta == 0 :
            root = (b/(2*a))
            return (root,)
        else:
            return()
        pass


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds

    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
