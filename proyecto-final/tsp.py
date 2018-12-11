from nodes import NodeGenerator
from simulated_annealing import SimulatedAnnealing
from brute_force import BruteForce
import numpy as np
from sklearn.model_selection import ParameterGrid


def main():
    '''define some global variables'''
    results = []
    '''set the simulated annealing algorithm params'''
    temp = list(range(100, 5000, 100))
    stopping_temp = [0.000000001, 0.00000001, 0.0000001, 0.000001, 0.00001]
    alpha = [a / 100 for a in range(1,100)]
    parameter_dict = {
    "temp": temp,
    "stopping_temp": stopping_temp,
    "alpha": alpha
    }
    stopping_iter = 10000000
    parameter_grid = ParameterGrid(parameter_dict)
    simulations = len(list(parameter_grid))

    '''set the dimensions of the grid'''
    size_width = 200
    size_height = 200

    '''set the number of nodes'''
    population_size = 5

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    for parameters in parameter_grid:
        temp = parameters['temp']
        stopping_temp = parameters['stopping_temp']
        alpha = parameters['alpha']
        sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
        initial_solution = sa.curr_solution
        sa.anneal()
        results.append((sa.min_weight, sa.iteration, parameters))

    print(results)

    '''run brute force solution'''
    # The same initial solution is used
    bf = BruteForce(nodes, initial_solution)
    bf.solve()

    # '''animate'''
    # sa.animateSolutions()
    #
    # '''show the improvement over time'''
    # sa.plotLearning()
    #
    # '''animate (brute force)'''
    # bf.animateSolutions()
    #
    # '''show the improvement over time (brute force)'''
    # bf.plotLearning()


if __name__ == "__main__":
    main()
