# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea
from MyProblem import MyProblem
import matplotlib.pyplot as plt


if __name__ == '__main__':
    problem = MyProblem()
    Encoding = 'RI'       # Encoding
    NIND = 20           # Population size
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # Create a region descriptor
    population = ea.Population(Encoding, Field, NIND) # Instantiate population object
    """================================Algorithm parameter settings============================="""
    myAlgorithm = ea.moea_NSGA3_DE_templet(problem, population) # Instantiate an algorithm template object
    myAlgorithm.MAXGEN = 25 # Maximum number of evolutions
    myAlgorithm.mutOper.F = 0.5 # The parameter F in differential evolution
    myAlgorithm.recOper.XOVR = 0.7 # Reorganization Probability
    myAlgorithm.drawing = 0
    """===========================Call algorithm template for population evolution======================="""
    NDSet = myAlgorithm.run ()  #
    NDSet.save ()  #
    #drawing
    print ( 'Seconds: %s' % (myAlgorithm.passTime) )
    print ( 'Non-dominated individuals：%s ' % (NDSet.sizes) )
    print ( 'Decision variable value：%s ' % (NDSet.Phen) )
    print ( 'Decision target value：%s ' % (NDSet.ObjV) )

    ax1 = plt.Circle ( (NDSet.Phen[-1,2], 2.5), NDSet.Phen[-1,0], fill=False )
    ax2 = plt.Rectangle ( (1, 2), 18, 1, fill=False )
    ax3 = plt.Circle ( (NDSet.Phen[-1,3], 13.5), NDSet.Phen[-1,1], fill=False )
    ax4 = plt.Rectangle ( (1, 13), 18, 1, fill=False )
    fig, ax = plt.subplots ()

    ax.add_artist ( ax1 )
    ax.add_artist ( ax2 )
    ax.add_artist ( ax3 )
    ax.add_artist ( ax4 )
    plt.title ( 'Arbeitsraum mit Abstand (2 Variablen)', fontsize=14 )
    plt.xlim ( 0, 20 )
    plt.ylim ( 0, 17 )
    ax.set_aspect ( 1 )

    plt.show ()

