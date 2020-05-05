#!/usr/bin/env python

import unittest
import numpy as np

from PyTrilinos import Epetra
from project3 import TwoDimLaplace


class TestLaplaceSolverMPI(unittest.TestCase):

    def setUp(self):

        self.comm = Epetra.PyComm()
        self.rank = self.comm.MyPID()

    def test_top_bcs(self):

        solver = TwoDimLaplace(self.comm, nx=4, ny=3)
        solver.set_boundary_condition(side='bottom', value=0)
        solver.set_boundary_condition(side='left', value=0)
        solver.set_boundary_condition(side='right', value=0)
        solver.set_boundary_condition(side='top', value=10)
        solver.load_balance()
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[0., 0., 0., 0.], [0., 2.647059,  2.647059,  0.], [10., 10., 10., 10.]]), atol=0.01) 

    def test_left_bc(self):

        solver = TwoDimLaplace(self.comm, nx=4, ny=4)
        solver.set_boundary_condition(side='bottom', value=0)
        solver.set_boundary_condition(side='right', value=0)
        solver.set_boundary_condition(side='top', value=0)
        solver.set_boundary_condition(side='left', value=7)
        solver.load_balance()
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[7., 0., 0., 0.], [7., 2.625, 0.875, 0.], [7., 2.625, 0.875, 0.], [7., 0., 0., 0.]]), atol=0.01)

    def test_right_bc(self):

        solver = TwoDimLaplace(self.comm, nx=4, ny=3)
        solver.set_boundary_condition(side='bottom', value=0)
        solver.set_boundary_condition(side='top', value=0)
        solver.set_boundary_condition(side='left', value=0)
        solver.set_boundary_condition(side='right', value=5)
        solver.load_balance()
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[0., 0., 0.,5.], [0., 0.57041, 1.782531, 5.],[0., 0., 0., 5.]]), atol=0.01)

    def test_bottom_bc(self):
        solver = TwoDimLaplace(self.comm, nx=3, ny=3)
        solver.set_boundary_condition(side='top', value=0)
        solver.set_boundary_condition(side='left', value=0)
        solver.set_boundary_condition(side='right', value=0)
        solver.set_boundary_condition(side='bottom', value=14)
        solver.load_balance()
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[14., 14., 14.], [0.,3.5,0.],[0.,0.,0.]]), atol=0.01)


if __name__ == '__main__':
    unittest.main()
