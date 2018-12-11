from simulated_annealing import SimulatedAnnealing
import numpy as np
from sklearn.model_selection import ParameterGrid
import matplotlib.pyplot as plt
import time
from optimize import optimal_run

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

    # Get optimal parameters from all sumulations:
    optimal_run_data = optimal_run(results)
    parameters = optimal_run_data[3]
    temp = parameters['temp']
    stopping_temp = parameters['stopping_temp']
    alpha = parameters['alpha']

    '''general plots'''

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

    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    start_time = time.time()
    sa.anneal()
    execution_time = time.time() - start_time

    print('Min weight: ', sa.min_weight)
    print('Iterations: ', sa.iteration)
    print('Execution time: ', execution_time)


    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()

if __name__ == "__main__":
    main()
