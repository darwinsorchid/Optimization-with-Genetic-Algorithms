'''
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
┆ @Created: 25-11-2024 14:20                                                                            ┆
┆ @Author: Alexandra Mpekou                                                                             ┆
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
┆ Building a Genetic Algorithm (GA) for optimization purposes.                                          ┆
┆ This particular GA was developed to maximize an objective function regarding the following problem:   ┆
┆                                                                                                       ┆
┆   "A company is considering three investments. Investment 1 will yield a net present value (NPV)      ┆
┆    of $16,000; investment 2, an NPV of $22,000 and investment 3, an NPV of $12,000. Each investment   ┆
┆    requires a certain cash outflow at the present time: investment 1, $5,000; investment 2,           ┆ 
┆    $7,000 and investment 3, $4,000. Currently, $10,000 is available for investment. Formulate         ┆
┆    a problem whose solution will tell the company how to maximize the NPV obtained from investments   ┆ 
┆    1-3."                                                                                              ┆
┆                                                                                                       ┆
┆    Variable type: Boolean                                                                             ┆
┆            xi(i = 1,2,3) = {1 if investment i is made | 0 otherwise }                                 ┆
┆                                                                                                       ┆ 
┆    Equation:     max z = 16x1 + 22x2 + 12x3                                                           ┆
┆    Constraints:                                                                                       ┆
┆                 • 5x1 + 7x2 + 4x3 ≤ 10                                                                ┆                                                                         ┆   
┆                                                                                                       ┆
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
'''


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Import Libraries ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
import numpy as np 
from geneticalgorithm import geneticalgorithm as ga


# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define Fitness Function ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

def fitness_function(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    # Define constraints and penalty
    penalty = 0
    if 5 * x1 + 7 * x2 + 4 * x3 > 10:
        penalty = np.inf

    # Make output negative because geneticalgorithm library is set up to MINIMIZE not MAXIMIZE
    return -(16 * x1 + 22 * x2 + 12 * x3 ) + penalty 

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Define model hyperparameters ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

# Need to include all of the model parameters

''' DEFAULT PARAMETER VALUES:

'max_num_iteration': None, 
'population_size': 100,
'mutation_probability': 0.5,
'elit_ratio': 0.01,
'crossover_probability': 0.5,
'parents_portion': 0.3,
'crossover_type': 'uniform',
'max_iteration_without_improv': None
'''

algorithm_params = {'max_num_iteration': None, 
                    'population_size': 100,
                    'mutation_probability': 0.5,
                    'elit_ratio': 0.01,
                    'crossover_probability': 0.5,
                    'parents_portion': 0.3,
                    'crossover_type': 'uniform',
                    'max_iteration_without_improv': None}

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Create Instance of GA model ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
model = ga(fitness_function, dimension = 3, variable_type = 'bool', algorithm_parameters = algorithm_params)

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ Run model with hyperparameters ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
model.run()