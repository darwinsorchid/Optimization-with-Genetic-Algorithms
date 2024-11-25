from genetic_algorithm import genetic_algorithm

# Hyper parameters
population_size = 1000
generations = 50

best_solution, best_fitness = genetic_algorithm(population_size, generations)

if best_solution is not None:
    print("Final best solution:", best_solution)
    print("Final best fitness:", best_fitness)
else:
    print("No feasible solution found within the given constraints.")