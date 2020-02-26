"""
A program that solves systems of linear equations.

by Jay Speidell for CS 417.

For more details, see README.md

To run the program, use the command:
> python main.py

"""

from solver import solve
from numpy import array

__all__ = ['main']

def main():
    """
    main()

    Includes hard-coded X, Xt, and Y arrays from the Quadratic example in the
    course material. Passes these to solve() and prints the return.
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
