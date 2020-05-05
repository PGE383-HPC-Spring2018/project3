#!/usr/bin/env python

from PyTrilinos import Epetra

class TwoDimLaplace():

    def __init__(self, comm, nx=10, ny=10, xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0):
        return

    def set_boundary_condition(self, side='top', value=0.0):
        return

    def load_balance(self):
        return

    def solve(self):
        return

    def get_solution(self):
        return


if __name__ == "__main__":

    comm = Epetra.PyComm()

    solver = TwoDimLaplace(comm, nx=100, ny=100, xmin=0, xmax=10, ymin=0, ymax=10)
    solver.load_balance()
    solver.set_boundary_condition(side="left", value=10)
    solver.set_boundary_condition(side="right", value=10)
    solver.set_boundary_condition(side="bottom", value=0)
    solver.set_boundary_condition(side="top", value=0)
    solver.solve()
    sol = solver.get_solution()
