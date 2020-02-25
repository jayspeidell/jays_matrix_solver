"""
A program that solves systems of linear equations. 

Depends on numpy.
"""

from solver import solve

from numpy import array

__all__ = ['main']

def main():
    """
    The main function!
    """
    X = array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ])
    Xt = array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ])
    Y = array([
                [0],
                [1],
                [4]
            ])

    _, phi_hat = solve(X, Xt, Y)

    print(phi_hat)


if __name__== "__main__":
  main()
