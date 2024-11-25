'''
┆┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┆
┆ @Created: 25-11-2024 12:30                                                                          ┆
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


from genetic_algorithm import genetic_algorithm
import streamlit as st

st.markdown("# Optimization with Genetic Algorithms")

# Hyper parameters
population_size = st.sidebar.slider("Choose population size", 100, 10000, step = 100)
generations = st.sidebar.slider("Choose number of generations", 10, 100, step = 20)

best_solution, best_fitness = genetic_algorithm(population_size, generations)

if best_solution is not None:
    st.write("Final best solution:", best_solution)
    st.write("Final best fitness:", best_fitness)
else:
    st.write("No feasible solution found within the given constraints.")