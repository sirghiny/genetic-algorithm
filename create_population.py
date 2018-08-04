from create_individual import *

def create_population(individual_size, population_size):
    return [create_individual(individual_size) for i in range(population_size)]

