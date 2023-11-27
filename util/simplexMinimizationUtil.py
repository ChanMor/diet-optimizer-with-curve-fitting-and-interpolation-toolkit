import numpy as np
import pandas as pd
from foodDataUtil import food_data, upper_limit, lower_limit, food_cost
import SimplexMethod as sm

selected_foods = ["Frozen Broccoli", "Carrots Raw", "Celery Raw", "Frozen Corn", "Lettuce, Iceberg, Raw", 
                  "Roasted Chicken", "Potatoes, Baked", "Tofu", "Peppers, Sweet, Raw", "Spaghetti W/ Sauce", 
                  "Tomato, Red, Ripe, Raw", "Apple, Raw, W/ Skin", "Banana", "Grapes", "Kiwifruit, Raw, Fresh", 
                  "Oranges", "Bagels", "Wheat Bread", "White Bread", "Oatmeal Cookies"]

def get_variables(foods):
    variables = []
    for i in range(len(foods)):
        variables.append(f"x{i+1}")

    for i in range(22 + len(foods)):
        variables.append(f"s{i+1}")
    variables.append("z")
    return variables

def format_matrix(matrix, variables):
    column_names = variables.copy()
    print(variables)
    column_names.extend(["RHS"])
    df = pd.DataFrame(matrix, columns= column_names)
    df.index +=1
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df)

def generate_slack_variables(index):
    slack_variables = []
    for i in range(22 + len(selected_foods) + 1):
        slack_variables.append(0)
    slack_variables[index] = 1
    return slack_variables



def generate_constraints_matrix(foods):
    matrix_coefficients = []
    for i in range(11):
        upper_constraints_coefficients = []
        for food in foods:
            upper_constraints_coefficients.append(food_data[food][i])

        upper_constraints_coefficients.extend(generate_slack_variables(i))
        upper_constraints_coefficients.append(upper_limit[i])
        matrix_coefficients.append(upper_constraints_coefficients)

    for i in range(11):
        lower_constraints_coefficients = []
        for food in foods:
            lower_constraints_coefficients.append(-1*food_data[food][i])

        lower_constraints_coefficients.extend(generate_slack_variables(i+11))
        lower_constraints_coefficients.append(-1*lower_limit[i])
        matrix_coefficients.append(lower_constraints_coefficients)
    
    for i in range(len(foods)):
        serving_coefficient = []
        for j in range(len(foods)):
            if i == j:
                serving_coefficient.append(1)
            else:
                serving_coefficient.append(0)
        serving_coefficient.extend(generate_slack_variables(i+22))
        serving_coefficient.append(10)

        matrix_coefficients.append(serving_coefficient)

    return np.array(matrix_coefficients)


def generate_objective_matrix(foods):
    objective_coefficients = []
    for food in foods:
        objective_coefficients.append(food_cost[food])
    objective_coefficients.extend(generate_slack_variables(22 + len(foods) ))
    objective_coefficients.extend([0])
    return np.array(objective_coefficients)





constraints_matrix = generate_constraints_matrix(selected_foods)
objective_matrix = generate_objective_matrix(selected_foods)
extended_matrix = np.vstack((constraints_matrix, objective_matrix))

variables = get_variables(selected_foods)
format_matrix(extended_matrix, variables)
# format_matrix(sm.preprocessing(extended_matrix), variables)
simplex_matrix = sm.simplex_method(extended_matrix)
format_matrix(simplex_matrix, variables)
solution = sm.get_solution(simplex_matrix)
print(solution)


# matrix = np.array([[-1.0, -2.0, 1.0, 0.0, 0.0, -4.0],
#                    [-7.0, -6.0, 0.0, 1.0, 0.0, -20.0],
#                    [14.0, 20.0, 0.0, 0.0, 1.0, 0.0]])
# print(sm.simplex_method(matrix))

# matrix = np.array([[ 2.0,   3.0,  4.0, 1.0, 0.0, 0.0, 0.0,  14.0],
#                    [-3.0,  -1.0, -5.0, 0.0, 1.0, 0.0, 0.0,  -4.0],
#                    [-1.0 , -4.0, -3.0, 0.0, 0.0, 1.0, 0.0,  -6.0],
#                    [ 4.0,   2.0,  1.0, 0.0, 0.0, 0.0, 1.0,  0.0]])
# print(sm.simplex_method(matrix))