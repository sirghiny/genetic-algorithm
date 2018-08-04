from imports import *

from variables import *
from get_fitness import *
from evaluate_population import *
from get_new_generation import *
from check_termination_condition import *



while termination is False:
    current_best_individual = get_fitness(best_individuals_stash[-1])
    print('Generation: ', generation_count)
    best_individuals = evaluate_population(current_population)
    current_population = get_new_generation(best_individuals)
    termination = check_termination_condition(current_best_individual, generation_count)
    generation_count += 1
else:
    print(get_fitness(best_individuals_stash[-1]))

