from imports import *

def generate_data():
    coeff = [0.4, -0.3, 0.2, -0.1]
    x = [[random() for j in range(len(coeff))] for i in range(1000)]
    y = [dot(i, coeff) for i in x]
    return array(x), array(y)

