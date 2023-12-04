import numpy as np
from .simplex_method_util import simplex_method

def find_identity(array):
    if 1 in array:
        instance_of_1 = [i for i, value in enumerate(array) if value == 1]
        return instance_of_1[0]
    return None
    
def is_identity(array, index):
    for i in range(len(array)):
        if i == index:
            continue
        if array[i] != 0:
            return False
    return True

def generate_solution_array(matrix):
    num_variables = matrix.shape[1] - 1
    solution = np.empty(num_variables)
    for i in range(num_variables):
        solution_index = find_identity(matrix[:, i])        
        if solution_index is not None and is_identity(matrix[:, i], solution_index):
            solution[i] = matrix[solution_index, -1]
        else:
            solution[i] = 0
    return solution

def generate_dictionary(foods):

    if foods == []:
        print("System: No Food Selected!")
        return None

    simplex_matrix = simplex_method(foods)

    if simplex_matrix == None:
        return None

    solution_array = generate_solution_array(simplex_matrix)

    rounded_solution_array = np.round(solution_array, decimals=2)
    food_dict = dict(zip(foods, rounded_solution_array))
    
    return food_dict