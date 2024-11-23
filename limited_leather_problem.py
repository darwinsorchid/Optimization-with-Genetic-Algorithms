'''
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
┆ @Created: 23-11-2024 18:09                                                                          ┆
┆ @Author: Alexandra Mpekou                                                                           ┆
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
┆ Building a Genetic Algorithm (GA) for optimization purposes.                                        ┆
┆ This particular GA was developed to maximize an objective function regarding the following problem: ┆
┆                                                                                                     ┆
┆    "Limited Leather manufactures two types of belts: the deluxe model and the regular model.        ┆
┆     Each type requires 1 sq yd of leather. A regular belt requires 1 hour of skilled labor,         ┆
┆     and a deluxe belt requires 2 hours. Each week, 40 sq yd of leather and 60 hours of skilled      ┆
┆     labor are available. Each regular belt contributes $3 to profit and each deluxe belt, $4.       ┆
┆     Formulate a mathematical model to maximize the profit."                                         ┆
┆                                                                                                     ┆
┆    Equation:     max z = 4x1 + 3x2                                                                  ┆
┆    Constraints:                                                                                     ┆
┆                 • x1 + x2 ≤ 40                                                                      ┆
┆                 • 2x1 + x2 ≤ 60                                                                     ┆
┆                 • x1, x2 ≥ 0                                                                        ┆ 
┆                                                                                                     ┆
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
'''


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Import Libraries ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
import random
import numpy as np 
import matplotlib.pyplot as plt


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define Objective Function ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

def objective_function(x1: int, x2: int) -> int:
    ''' Function that describes the problem and is going to be maximized by the genetic algorithm.
        Takes as input an integer for each variable x1 and x2.
        Returns the output of the objective function z = 4x1 + 3x2.
    '''

    return 4*x1 + 3*x2


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define Constraints ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

def constraint1(x1: int, x2: int) -> bool:
    ''' Checks for the first constraint that is described by the problem: • x1 + x2 ≤ 40 
    '''
    return x1 + x2 <= 40


def constraint2(x1: int, x2: int) -> bool:
    ''' Checks for the second constraint that is described by the problem: • 2x1 + x2 ≤ 60 
    '''
    return 2*x1 + x2 <= 60


def constraint3(x1: int, x2: int) -> bool:
    ''' Checks for the third constraint that is described by the problem: • x1, x2 ≥ 0
    '''
    return x1 >=0 and x2 >= 0


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define GA function ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

def genetic_algorithm(population_size: int, generation_number: int):

    # Initialization of population individuals
    population = []
    
    for i in range(population_size):
        x1 = random.uniform(0,40) # Max value of x1 as defined by constraints 1, 2
        x2 = random.uniform(0,60) # Max value of x2 as defined by constraints 1, 2

        population.append(x1, x2) # Create a list of tuples as the population of the algorithm
    
    # Initialize optimization variables
    best_solution = None
    best_fitness = float('-inf')