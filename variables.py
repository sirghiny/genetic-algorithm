from imports import *

from generate_data import *
from multiple_linear_regression import *
from create_individual import *
from create_population import *

inputs, outputs = generate_data()
individual_size = len(inputs[0])
population_size = 1000
selection_size = floor(0.1*population_size)
max_generations = 50
probability_of_individual_mutating = 0.1
probability_of_gene_mutating = 0.25
best_possible = multiple_linear_regression(inputs, outputs)
best_individuals_stash = [create_individual(individual_size)]
initial_population = create_population(individual_size, 1000)
current_population = initial_population
termination = False
generation_count = 0

