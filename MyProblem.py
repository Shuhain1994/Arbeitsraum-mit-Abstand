# -*- coding: utf-8 -*-

import numpy as np
import geatpy as ea
import math

"""
    Ich definiere den Arbeitsraum des 2-achsigen-Roboters als f, x1, x2 als 2 Achsen.
    max f=1/12*math.pi*x2*x1**2
    s.t.
    x1 + x2 = 10
    2 <= x1 <= 8
    1 <= x2 <= 6
"""


class MyProblem ( ea.Problem ):
    def __init__(self):
        name = 'MyProblem'
        M = 1  # Initialize M (target dimension)
        maxormins = [0]  # Initialize maxormins ( 1: minimize the target; -1: maximize the target)
        Dim = 2  # Initialize Dim (dimension of decision variable)
        varTypes = [0] * Dim
        # Initialize varTypes (types of decision variables, element 0 means continuous; 1 means discrete)
        lb = [2, 1]  # Lower bound of decision variables
        ub = [8, 6]  # Upper bound of decision variable
        lbin = [1, 1]  # 0 means not including the lower boundary of the variable, 1 means including
        ubin = [1, 1]  # 0 means not including the upper boundary of the variable, 1 means including
        # Call the parent class constructor to complete the instantiation
        ea.Problem.__init__ ( self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin )

    def aimFunc(self, pop):  # Objective function
        Vars = pop.Phen  # Get the decision variable matrix
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        pop.ObjV = 1 / 12 * math.pi * x2 * x1 ** 2
        # Calculate the objective function value and assign it to the ObjV attribute of the pop population object
        # Processing constraints
        pop.CV = np.hstack ( [np.abs ( x1 + x2 - 10 )] )