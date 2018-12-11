import random

def optimal_run(results):
    ''' Get the optimum from all simulations '''

    # First, optimize weight
    weights, iterations, execution_times, parameters = zip(*results)
    weights = list(weights)
    min_weight = min(weights)
    filtered = [result for result in results if result[0] == min_weight]

    # Second, optimize iterations
    weights, iterations, execution_times, parameters = zip(*filtered)
    iterations = list(iterations)
    min_iterations = min(iterations)
    filtered = [result for result in results if result[1] == min_iterations]

    # Finally, optimize running time
    weights, iterations, execution_times, parameters = zip(*filtered)
    execution_times = list(execution_times)
    min_execution_time = min(execution_times)
    filtered = [result for result in results if result[2] == min_execution_time]

    optimum = random.choice(filtered)

    return optimum
