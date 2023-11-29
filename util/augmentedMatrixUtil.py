import numpy as np
from foodDataUtil import food_data, upper_limit, lower_limit, food_cost

def get_variables(foods):
    variables = []
    for i in range(len(foods)):
        variables.append(f"x{i+1}")

    for i in range(22 + len(foods)):
        variables.append(f"s{i+1}")
    variables.append("z")
    return variables

def generate_slack_variables(index, foods):
    slack_variables = []
    for i in range(22 + len(foods) + 1):
        slack_variables.append(0)
    slack_variables[index] = 1
    return slack_variables

def generate_maximum_constraints(foods):
    matrix_coefficients = []
    for i in range(11):
        upper_constraints_coefficients = []
        for food in foods:
            upper_constraints_coefficients.append(food_data[food][i])

        upper_constraints_coefficients.extend(generate_slack_variables(i, foods))
        upper_constraints_coefficients.append(upper_limit[i])
        matrix_coefficients.append(upper_constraints_coefficients)

    return np.array(matrix_coefficients)

def generate_minimum_constraints(foods):
    matrix_coefficients = []
    for i in range(11):
        lower_constraints_coefficients = []
        for food in foods:
            lower_constraints_coefficients.append(-1*food_data[food][i])

        lower_constraints_coefficients.extend(generate_slack_variables(i+11, foods))
        lower_constraints_coefficients.append(-1*lower_limit[i])
        matrix_coefficients.append(lower_constraints_coefficients)
    
    return np.array(matrix_coefficients)

def generate_serving_constraints(foods):
    matrix_coefficients = []
    for i in range(len(foods)):
        serving_coefficient = []
        for j in range(len(foods)):
            if i == j:
                serving_coefficient.append(1)
            else:
                serving_coefficient.append(0)
        serving_coefficient.extend(generate_slack_variables(i+22, foods))
        serving_coefficient.append(10)
        matrix_coefficients.append(serving_coefficient)
    
    return np.array(matrix_coefficients)

def generate_constraints_matrix(foods):
    upper_constraints = generate_maximum_constraints(foods)
    lower_constraints = generate_minimum_constraints(foods)
    serving_constraints = generate_serving_constraints(foods)

    constraints_matrix = np.vstack((upper_constraints, lower_constraints, serving_constraints))
    return constraints_matrix

def generate_objective_matrix(foods):
    objective_coefficients = []
    for food in foods:
        objective_coefficients.append(food_cost[food])
    objective_coefficients.extend(generate_slack_variables(22 + len(foods) , foods))
    objective_coefficients.extend([0])
    return np.array(objective_coefficients)

def generate_augmented_matrix(foods):
    constraints_matrix = generate_constraints_matrix(foods)
    objective_matrix = generate_objective_matrix(foods)
    
    return np.vstack((constraints_matrix, objective_matrix))





# matrix = np.array([[-1.0, -2.0, 1.0, 0.0, 0.0, -4.0],
#                    [-7.0, -6.0, 0.0, 1.0, 0.0, -20.0],
#                    [14.0, 20.0, 0.0, 0.0, 1.0, 0.0]])
# print(sm.simplex_method(matrix))

# matrix = np.array([[ 2.0,   3.0,  4.0, 1.0, 0.0, 0.0, 0.0,  14.0],
#                    [-3.0,  -1.0, -5.0, 0.0, 1.0, 0.0, 0.0,  -4.0],
#                    [-1.0 , -4.0, -3.0, 0.0, 0.0, 1.0, 0.0,  -6.0],
#                    [ 4.0,   2.0,  1.0, 0.0, 0.0, 0.0, 1.0,  0.0]])
# print(sm.simplex_method(matrix))