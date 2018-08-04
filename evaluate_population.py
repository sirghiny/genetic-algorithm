from imports import *
from get_fitness import *
from variables import inputs, selection_size, best_individuals_stash

def evaluate_population(population):
    fitness_list = [get_fitness(individual)
                    for individual in tqdm(population)]
    error_list = sorted(fitness_list, key=lambda i: i['error'])
    best_individuals = error_list[: selection_size]
    best_individuals_stash.append(best_individuals[0]['coeff'])
    print('Error: ', best_individuals[0]['error'],
          'COD: ', best_individuals[0]['COD'])
    return best_individuals

