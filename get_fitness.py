from imports import *
from variables import inputs, outputs

def get_fitness(individual):
    predicted_outputs = dot(array(inputs), array(individual))
    output_mean = mean(outputs)
    SST = array(
        [(i - output_mean) ** 2 for i in outputs]
        ).sum()
    SSR = array(
        [(i - j) ** 2 for i, j in zip(outputs, predicted_outputs)]
        ).sum()
    COD = (1 - (SSR / SST)) * 100.0
    average_error = (SSR / len(outputs))
    return {'COD': COD, 'error': average_error, 'coeff': individual}

