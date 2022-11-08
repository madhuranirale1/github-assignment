"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
"""
import numpy as np
from numpy import unravel_index


def max_index(X):

    if not isinstance(X, np.ndarray):
        raise ValueError('input must be a numpy array')
    if len(X.shape) != 2:
        raise ValueError('not a 2-D array')
    i = 0
    j = 0
    i, j = unravel_index(X.argmax(), X.shape)

    return i, j


def wallis_product(n_terms):
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000.
    pi = 2.0
    if (n_terms == 0):
        return 2
    if (n_terms == 1):
        pi = pi * (4 * 1)/(4 * 1 - 1)
        return pi
    for i in range(1, n_terms):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi
