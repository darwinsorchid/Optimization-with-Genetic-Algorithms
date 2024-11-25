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