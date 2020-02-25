"""
Contains a driver function to demonstrate the functions developed for this
assignment.
"""

from numpy import array, concatenate
from multiply import multiply

__all__ = ['rref']

def solve():
    """
    A driver function to solve the system of linear equations.

    For this assignment, it is simply hard-coded to demonstrate the
    functions developed.
    """
    X = array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ])
    Xt = array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ])
    Y = array([
                [0],
                [1],
                [4]
            ])

    XtX = multiply(Xt,X)
    XtY = multiply(Xt,Y)

    arr = concatenate((XtX, XtY), axis=1)
