# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea
from MyProblem import MyProblem

if __name__ == '__main__':

    problem = MyProblem()

    Encoding = 'RI'       # Encoding
    NIND = 100            # Population size
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # Create a region descriptor
    population = ea.Population(Encoding, Field, NIND) # Instantiate population object
    """================================Algorithm parameter settings============================="""
    myAlgorithm = ea.soea_DE_rand_1_bin_templet(problem, population) # Instantiate an algorithm template object
    myAlgorithm.MAXGEN = 200 # Maximum number of evolutions
    myAlgorithm.mutOper.F = 0.5 # The parameter F in differential evolution
    myAlgorithm.recOper.XOVR = 0.7 # Reorganization Probability
    """===========================Call algorithm template for population evolution======================="""
    [population, obj_trace, var_trace] = myAlgorithm.run() # Execute algorithm template
    population.save() # Save the information of the last generation population to a file
    # Output result
    best_gen = np.argmin(problem.maxormins * obj_trace[:, 1]) # Record the generation of the best population individual
    best_ObjV = obj_trace[best_gen, 1]
    print('Der optimale Zielfunktionswert ist：%s'%(best_ObjV))
    print('Der optimale Wert für die Variable ist：')
    for i in range(var_trace.shape[1]):
        print(var_trace[best_gen, i])
    print('Anzahl der effektiven Evolutionen：%s'%(obj_trace.shape[0]))
    print('Die beste Generation ist die %s Generation'%(best_gen + 1))
    print('Anzahl der Bewertungen：%s'%(myAlgorithm.evalsNum))
    print('Zeitaufwand %s sek'%(myAlgorithm.passTime))
