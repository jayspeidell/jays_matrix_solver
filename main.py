"""
A program that solves systems of linear equations.

by Jay Speidell for CS 417

See README.md for details.
"""

from numpy import array
from solver import solve

__all__ = ['main'] # suppresses pydoc from documenting imported assets 

def main():
    """
    main()

    Provides the sample arrays X, Xt, and Y provided in the Quadratic example,
    passes them to solve(), and prints the return.

    Parameters
    -------
    none

    Returns
    -------
    none
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
