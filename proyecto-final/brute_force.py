import math
import random
import itertools
import matplotlib.pyplot as plt
import utils
import visualizer

class BruteForce:
    def __init__(self, coords, initial_solution):
        '''
        Brute force solution for the TSP.
        '''
        self.coords = coords
        self.initial_solution = initial_solution
        self.iteration = 1

        self.dist_matrix = utils.vectorToDistMatrix(coords)
        self.curr_solution = self.initial_solution
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

        print('Intial weight: ', self.curr_weight)

    def weight(self, sol):
        '''
        Calcuate weight
        '''
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def accept(self, candidate):
        '''
        Accept with probability 1 if candidate solution is better than
        current solution.
        '''
        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate

    def solve(self):
        for permutation in itertools.permutations(self.initial_solution[1:]):
            candidate = [self.initial_solution[0]] + list(permutation)
            self.accept(candidate)
            self.iteration += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)

        print('Minimum weight: ', self.min_weight)
        print('Improvement: ',
              round((self.initial_weight - self.min_weight) / (self.initial_weight), 4) * 100, '%')

    def animateSolutions(self):
        visualizer.animateTSP(self.solution_history, self.coords)

    def plotLearning(self):
        plt.plot([i for i in range(len(self.weight_list))], self.weight_list)
        line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        plt.legend([line_init, line_min], ['Initial weight', 'Optimized weight'])
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.show()
