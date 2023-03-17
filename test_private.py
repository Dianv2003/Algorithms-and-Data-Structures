"""
    - test_private.py
    -
    - Algorithms and Data Structures
    - Assignment 1
    - Dian achternaam studentnummer
    - Tjarda Leppers s3642844
    -
    - This file contains (private) unit tests for the CSP functions defined in csp.py.
"""

import unittest
import numpy as np

from csp import CSP


class PrivateTestCSP(unittest.TestCase):

    def test_satisfies_sum_constraint(self):
        """
        This unittest checks if the satisfies_sum_constraint function correctly handles a None (sum)constraint.
        """

        groups = [[(0,0), (0,1), (1,0), (1,1)]]
        constraints = None
        grid = np.array([
                [1, 1],
                [1, 1]
            ])
        csp = CSP(grid, numbers={2}, groups=groups, constraints=constraints)
        for group in groups:
            result = csp.satisfies_sum_constraint(group, constraints)
            self.assertTrue(result)


    def test_satisfies_count_constraint(self):
        """
        This unittest checks if the satisfies_count_constraint function correctly handles a None (count)constraint.
        """

        groups = [[(0,0), (0,1), (1,0), (1,1)]]
        constraints = None
        grid = np.array([
                [1, 1],
                [1, 1]
            ])
        csp = CSP(grid, numbers={2}, groups=groups, constraints=constraints)
        for group in groups:
            result = csp.satisfies_count_constraint(group, constraints)
            self.assertTrue(result)


    def test_satisfies_group_constraint(self):
        """
        This unittest checks if the satisfies_group_constraint function correctly handles None constraints.
        """

        groups = [[(0,0), (0,1), (1,0), (1,1)]]
        constraints = None
        grid = np.array([
                [1, 1],
                [1, 1]
            ])
        csp = CSP(grid, numbers={2}, groups=groups, constraints=constraints)
        result = csp.satisfies_group_constraints(list(range(len(groups))))
        self.assertTrue(result)
