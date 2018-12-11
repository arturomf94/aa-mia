from nodes import NodeGenerator
from simulated_annealing import SimulatedAnnealing
from brute_force import BruteForce
import numpy as np


def main():
    '''set the simulated annealing algorithm params'''
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000000

    '''set the dimensions of the grid'''
    size_width = 200
    size_height = 200

    '''set the number of nodes'''
    population_size = 12

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    initial_solution = sa.curr_solution
    sa.anneal()

    '''run brute force solution'''
    # The same initial solution is used
    bf = BruteForce(nodes, initial_solution)
    bf.solve()

    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()

    '''animate (brute force)'''
    bf.animateSolutions()

    '''show the improvement over time (brute force)'''
    bf.plotLearning()


if __name__ == "__main__":
    main()
