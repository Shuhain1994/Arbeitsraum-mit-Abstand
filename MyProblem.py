# -*- coding: utf-8 -*-

import numpy as np
import geatpy as ea
import math

"""
    Arbeitsraum =4/3*math.pi*(x1**3+x2**3)
    Position Anlage= np.linalg.norm(p1 - p2)
    s.t.
    x1 + x2 <= 14
    2 <= x1 <= 8
    4 <= x2 <= 9
    2 <= x3, x4 <= 18
    x1 + x2 - 2 <= sqrt (p1**2 + p2**2) <= x1 + x2 + 5 
"""


class MyProblem ( ea.Problem ):
    def __init__(self, M=2):
        name = 'MyProblem'
        M = 2  # Initialize M (target dimension)
        maxormins = [0, 0]  # Initialize maxormins ( 1: minimize the target; -1: maximize the target)
        Dim = 4  # Initialize Dim (dimension of decision variable)
        varTypes = [0] * Dim
        # Initialize varTypes (types of decision variables, element 0 means continuous; 1 means discrete)
        lb = [2, 4, 2, 2]  # Lower bound of decision variables
        ub = [8, 9, 18, 18]  # Upper bound of decision variable
        lbin = [1, 1, 1, 1]  # 0 means not including the lower boundary of the variable, 1 means including
        ubin = [1, 1, 1, 1]  # 0 means not including the upper boundary of the variable, 1 means including
        # Call the parent class constructor to complete the instantiation
        ea.Problem.__init__ ( self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin )

    def aimFunc(self, pop):  # Objective function
        Vars = pop.Phen  # Get the decision variable matrix
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        p1 = np.array ( [x3, 2.5], dtype=object)
        p2 = np.array ( [x4, 13.5], dtype=object)
        f2 = np.linalg.norm(p1 - p2)
        f1 = 2 * math.pi * (x1 ** 3 + x2 ** 3)
        pop.ObjV = np.hstack ( [f1, f2] )
        # Calculate the objective function value and assign it to the ObjV attribute of the pop population object
        # Processing constraints
        pop.CV = np.hstack ( [ x1 + x2 - 14, np.linalg.norm(p1 - p2)- x1 - x2 - 5, x1 + x2 - 2 - np.linalg.norm(p1 - p2)] )