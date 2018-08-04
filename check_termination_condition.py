from variables import max_generations

def check_termination_condition(best_individual, generation_count):
    if ((best_individual['COD'] >= 98.0)
            or (generation_count == max_generations)):
        return True
    else:
        return False

