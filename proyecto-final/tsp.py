from nodes import NodeGenerator
from simulated_annealing import SimulatedAnnealing
from brute_force import BruteForce
import numpy as np
from sklearn.model_selection import ParameterGrid
import matplotlib.pyplot as plt
import time


def main():
    '''define some global variables'''
    results = []
    '''set the simulated annealing algorithm parameter grid'''
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
    parameter_size = len(list(parameter_grid))

    '''set the dimensions of the grid'''
    size_width = 200
    size_height = 200

    '''set the number of nodes'''
    population_size = 12

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    ordered_temp = []
    ordered_stopping_temp = []
    ordered_alpha = []
    for parameters in parameter_grid:
        temp = parameters['temp']
        stopping_temp = parameters['stopping_temp']
        alpha = parameters['alpha']
        ordered_temp.append(temp)
        ordered_stopping_temp.append(stopping_temp)
        ordered_alpha.append(alpha)
        sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
        initial_solution = sa.curr_solution
        start_time = time.time()
        sa.anneal()
        execution_time = time.time() - start_time
        results.append((sa.min_weight, sa.iteration, execution_time, parameters))

    weights, iterations, execution_times, parameters = zip(*results)
    weights = list(weights)
    iterations = list(iterations)
    execution_times = list(execution_times)
    simulations = list(range(parameter_size))

    '''run brute force solution'''
    # The same initial solution is used
    bf = BruteForce(nodes, initial_solution)
    start_time = time.time()
    bf.solve()
    bf_execution_time = time.time() - start_time
    bf_min_weight = bf.min_weight
    bf_iterations = bf.iteration

    '''general plots'''

    plt.scatter(simulations, ordered_temp)
    plt.title('Temperatura')
    plt.ylabel('Temperatura')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, ordered_stopping_temp)
    plt.title('Temperatura Limite')
    plt.ylabel('Temperatura')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, ordered_alpha)
    plt.title('Alpha')
    plt.ylabel('Alpha')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, weights)
    plt.title('Distancias Finales')
    plt.ylabel('Distancia')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, iterations)
    plt.title('Iteraciones Totales')
    plt.ylabel('Numero de Iteraciones')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, execution_times)
    plt.title('Tiempos de Ejecucion')
    plt.ylabel('Tiempo')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, weights)
    line_bf = plt.axhline(y = bf_min_weight, color='r', linestyle='--')
    plt.legend([line_bf], ['Distancia con Fuerza Bruta'])
    plt.title('Distancias Finales')
    plt.ylabel('Distancia')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, iterations)
    line_bf = plt.axhline(y = bf_iterations, color='r', linestyle='--')
    plt.legend([line_bf], ['Iteraciones con Fuerza Bruta'])
    plt.title('Iteraciones Totales')
    plt.ylabel('Numero de Iteraciones')
    plt.xlabel('Simulacion')
    plt.show()

    plt.scatter(simulations, execution_times)
    line_bf = plt.axhline(y = bf_execution_time, color='r', linestyle='--')
    plt.legend([line_bf], ['Tiempo con Fuerza Bruta'])
    plt.title('Tiempos de Ejecucion')
    plt.ylabel('Tiempo')
    plt.xlabel('Simulacion')
    plt.show()

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
