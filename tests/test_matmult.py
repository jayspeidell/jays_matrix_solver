import pytest
from numpy import array, matmul

from matmult import multiply, something

@pytest.mark.parametrize(
    'lhs, rhs', [
    (
        array([
            [2,3,4,5],
            [4,1,4,6],
            [6,3,6,7],
            [8,7,6,5]]),
        array([
            [6,6,3,3],
            [7,4,8,2],
            [3,6,8,4],
            [9,8,3,5]])
    ),
    (
        array([
            [2,6,2,5],
            [4,7,7,6],
            [6,8,3,7],
            [8,3,1,5]]),
        array([
            [6,3,3],
            [4,8,1],
            [6,3,4],
            [8,3,5]])
    )])
def test_multiply(lhs,rhs):
    assert multiply(lhs, rhs).all() == matmul(lhs, rhs).all()

@pytest.mark.parametrize(
    'a, b', [(5,25),
                (4,20),
                (6,30) ]

)
def test_something(a,b):
    assert something(a) == b
