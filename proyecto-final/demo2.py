from simulated_annealing import SimulatedAnnealing
import numpy as np
from sklearn.model_selection import ParameterGrid
import matplotlib.pyplot as plt
import time

def main():
    '''define some global variables'''
    results = []
    '''set the simulated annealing algorithm parameter grid'''
    temp = 50000
    stopping_temp = 0.000000001
    alpha = .999
    stopping_iter = 10000000

    '''generate random list of nodes'''
    nodes = np.array([[20,20],
                        [60,20],
                        [100,40],
                        [120,80],
                        [160,20],
                        [200,40],
                        [180,60],
                        [180,100],
                        [140,140],
                        [200,160],
                        [180,200],
                        [140,180],
                        [100,160],
                        [80,180],
                        [60,200],
                        [20,160],
                        [40,120],
                        [100,120],
                        [60,80],
                        [20,40]])

    nodes = np.random.permutation(nodes)

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    start_time = time.time()
    sa.anneal()
    execution_time = time.time() - start_time


    '''general plots'''
    print('Min weight: ', sa.min_weight)
    print('Iterations: ', sa.iteration)
    print('Execution time: ', execution_time)

    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()

if __name__ == "__main__":
    main()
