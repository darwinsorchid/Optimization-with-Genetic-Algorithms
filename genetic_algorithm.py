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
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


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

'''
def constraint3(x1: int, x2: int) -> bool:
     Checks for the third constraint that is described by the problem: • x1, x2 ≥ 0
    
    return x1 >=0 and x2 >= 0
'''

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define GA function ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

def genetic_algorithm(population_size: int, generations: int):

    # Initialization of population individuals
    population = []
    fitness_history = []

    for i in range(population_size):
        # random.uniform generates a floating point number within a specific range and includes the limits of the range [a,b]
        x1 = random.uniform(0,40) # Max value of x1 as defined by constraints 1, 2
        x2 = random.uniform(0,60) # Max value of x2 as defined by constraints 1, 2

        population.append((x1, x2)) # Create a list of tuples as the population of the algorithm
    
    # Initialize optimization variables
    best_solution = None
    best_fitness = float('-inf')

    for generation in range(generations):

        # **Evaluation** of possible solutions
        # Create list of fitness for each individual (tuple of solutions) of the population --> fitness = output of objective function 
        fitness = [objective_function(x1, x2) for x1, x2 in population]

        # Create list of feasible population: individuals/tuples of x1, x2 values that satisfy the constraints 1 and 2
        feasible_pop = [individual for individual in population if constraint1(individual[0], individual[1]) and constraint2(individual[0], individual[1])]


        # **Selection** : select individuals with higher fitness values to become parents of next gen
        # Check if feasible population exists
        if feasible_pop:
            feasible_fitness = [objective_function(x1, x2) for x1, x2 in feasible_pop]

            # Individuals with higher fitness values have higher probability of being chosen as parents of next gen
            # k - number of individuals being selected
            parents = random.choices(feasible_pop, weights = feasible_fitness, k = population_size) 
        else:
            parents = []
            while len(parents) < population_size:
                potential_parents = random.choices(population, weights = fitness)
                if constraint1(potential_parents[0], potential_parents[1]) and constraint2(potential_parents[0], potential_parents[1]):
                    parents.append(potential_parents)

        
        # **Mating / Crossover** to create offsprings
        offsprings = []
        for i in range(population_size):
            # Randomly choose two parents from parents list
            parent1, parent2 = random.choices(parents, k = 2)
            # Randomly choose values for x1 and x2 of next geneneration based on the range formed by the max and minimum x1, x2 values of the parents
            x1_child = random.uniform(min(parent1[0], parent2[0]), max(parent1[0], parent2[0]))
            x2_child = random.uniform(min(parent1[1], parent2[1]), max(parent1[1], parent2[1]))
            offsprings.append((x1_child, x2_child))
        
        # **Mutation**
        ''' Define dynamic mutation rate
            • In the first generations: 
            High exploration / Low exploitation - High mutation rate 

            • In later generations:
            Low exploration / High exploitation - Low mutation rate
            '''
        mutation_rate = 1/(generation + 1) # Mutation rate decreases as the generation number increases
        
        for i in range(population_size):
            ''' • If randomly selected number is less than the mutation rate --> mutation happens for offspring: (x1_new, x2_new)
                • Else --> no mutation happens for offspring
               random.random() generates a floating point number between 0 and 1 [0,1) - includes 0 but not 1 
               '''

            if random.random() < mutation_rate:
                # Assign random values for x1, x2 of child
                offsprings[i] = (random.uniform(0, 40), random.uniform(0, 60))

        # **Elitism** 
        if best_solution is not None:
            offsprings[0] = best_solution
        
        # Assign offsprings of current generation as parents of the next generation
        population = offsprings

        # Find optimal solution 
        feasible_solutions = [(x1, x2) for (x1, x2) in population if constraint1(x1, x2) and constraint2(x1, x2)]

        if feasible_solutions:
            best_solution = max(feasible_solutions, key = lambda x: objective_function(x[0], x[1]))
            best_fitness = objective_function(best_solution[0], best_solution[1])
        fitness_history.append(best_fitness)

        # st.write(f"Generation {generation + 1}: Best solution: {best_solution} \nBest fitness: {best_fitness}.")
        


    # Plot the fitness progress
    fig = plt.figure(figsize = (10,10))

    plt.style.use("dark_background")

    fig.patch.set_facecolor('#030305')

    plt.plot(range(generation + 1), fitness_history)

    plt.title("Fitness Progress", color = '#ecd9fa')

    plt.xlabel("Generations", color = '#ecd9fa')
    plt.ylabel("Fitness", color = '#ecd9fa')

    plt.xticks(color = '#ecd9fa')
    plt.yticks(color = '#ecd9fa')

    st.pyplot(fig)

    
    return best_solution, best_fitness