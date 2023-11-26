import numpy as np
import pandas as pd
import augmentedMatrixUtil as am
from foodDataUtil import food_data, upper_limit, lower_limit

def find_pivot_column(array):
    negative_indices = np.where(array < 0)[0]
    if negative_indices.size > 0:
        pivot_col = negative_indices[np.argmax(np.abs(array[negative_indices]))]
        return pivot_col
    return None

def get_test_ratio(array, solution_column):
    test_ratio = np.empty(len(array))
    for i in range(len(array)):
        if array[i] == 0:
            test_ratio[i] = None
        else:
            test_ratio[i] = solution_column[i]/array[i]
    return test_ratio

def find_pivot_row_index(array, solution_column):
    test_ratio = get_test_ratio(array, solution_column)
    min_positive_index = np.where(test_ratio == np.min(test_ratio[test_ratio > 0]))[0]
    return min_positive_index[0]

def find_identity(array):
    if 1 in array:
        instance_of_1 = np.where(array == 1)[0]
        if instance_of_1.size == 1:
            return instance_of_1.item()
        return instance_of_1[0].item()
    return None
    
def is_identity(array, index):
    for i in range(len(array)):
        if i == index:
            continue
        if array[i] != 0:
            return False
    return True

def get_solution(matrix):
    num_variables = matrix.shape[1] - 1
    solution = np.empty(num_variables)
    for i in range(num_variables):
        solution_index = find_identity(matrix[:, i])        
        if solution_index is not None and is_identity(matrix[:, i], solution_index):
            solution[i] = matrix[solution_index, -1]
        else:
            solution[i] = 0
    return solution


def simplex_method(variables, constraints):
    matrix = am.get_augmented_coefficient_matrix(variables, constraints)

    iteration_count = 0
    while iteration_count < 1000:
        last_row = matrix[-1,:]
        solution_column = matrix[:,-1]

        pivot_column_index = find_pivot_column(last_row)
        if pivot_column_index == None:
            break
        
        pivot_column = matrix[:, pivot_column_index]
        pivot_row_index = find_pivot_row_index(pivot_column, solution_column)
        matrix[pivot_row_index,:] /= matrix[pivot_row_index, pivot_column_index]

        number_of_rows = matrix.shape[0]
        for i in range(number_of_rows):
            if i == pivot_row_index:
                continue
            normalized_row = matrix[i, pivot_column_index]*matrix[pivot_row_index,:]
            matrix[i,:] -= normalized_row
        iteration_count += 1

    return matrix

def generate_constraints_equations(foods):
    function_equations = []
    for i in range(11): 
        equation = ""
        for j, food in enumerate(foods, start=1):
            if j == 1:
                equation += f"{food_data[food][i]} * x{j}"
            else:
                equation += f" + {food_data[food][i]} * x{j}"
        function_equations.append(equation.strip())

    return function_equations

def get_variables(foods):
    variables = []
    for i in range(len(foods)):
        variables.append(f"x{i+1}")
    return variables

def generate_system_equations(constraints_equations):
    system = []
    for i, eq in enumerate(constraints_equations, start=0):
        upper_eq = f"{eq} + -{upper_limit[i]}"
        lower_eq = f"{eq} + -{lower_limit[i]}"
        system.append(lower_eq)
        system.append(upper_eq)
    return system

def format_matrix(matrix, variables):
    column_names = variables.copy()
    column_names.extend(["RHS"])
    df = pd.DataFrame(matrix, columns= column_names)
    df.index += 1
    print(df)

def format_solution(solution, variables):
    column_names = variables
    df = pd.DataFrame([solution], columns=column_names)
    df.index += 1 
    print(df)

selected_foods = ["Frozen Broccoli", "Carrots Raw", "Tofu", "Tomato Soup"]
function_equations = generate_constraints_equations(selected_foods)
system = generate_system_equations(function_equations)
variables = get_variables(selected_foods)
simplex_matrix = simplex_method(variables, system)

format_matrix(simplex_matrix, variables)
format_solution(get_solution(simplex_matrix), variables)


