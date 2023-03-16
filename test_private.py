import typing
import unittest
import numpy as np

from csp import CSP


class PrivateTestCSP(unittest.TestCase):

    def test_satisfies_sum_constraint(self):
        """
        This unit test checks if the function satisfies_sum_constraint correctly
        handles a None (sum)constraint.
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
        This unit test checks if the function satisfies_count_constraint correctly
        handles a None (count)constraint.
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
        This unit test checks if the function satisfies_group_constraint correctly
        handles None constraints.
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
