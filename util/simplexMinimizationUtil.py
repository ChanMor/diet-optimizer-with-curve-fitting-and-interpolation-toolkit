import numpy as np
import pandas as pd
from foodDataUtil import food_data, upper_limit, lower_limit, food_cost
import SimplexMethod as sm

def generate_maximum_constraints_equations(foods):
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

def generate_manimum_constraints_equations(foods):
    function_equations = []
    for i in range(11): 
        equation = ""
        for j, food in enumerate(foods, start=1):
            if j == 1:
                equation += f"-{food_data[food][i]} * x{j}"
            else:
                equation += f" + -{food_data[food][i]} * x{j}"
        function_equations.append(equation.strip())

    return function_equations

def get_variables(foods):
    variables = []
    for i in range(len(foods)):
        variables.append(f"x{i+1}")

    for i in range(22):
        variables.append(f"s{i+1}")
    variables.append("z")
    return variables

def generate_system_equations(constraints_equations):
    maximum_constraints = constraints_equations[:11]
    manimum_constraints = constraints_equations[11:]
    
    system = []
    for i, eq in enumerate(maximum_constraints, start=0):
        upper_eq = f"{eq} + -{upper_limit[i]}"
        system.append(upper_eq)
    for j, eq in enumerate(manimum_constraints, start=0):
        lower_eq = f"{eq} + {lower_limit[j]}"
        system.append(lower_eq)

    return system

def format_matrix(matrix, variables):

    column_names = variables.copy()
    column_names.extend(["RHS"])
    df = pd.DataFrame(matrix, columns= column_names)
    df.index = ["Calories", "Cholesterol", "Total Fat",
                "Sodium", "Carbohydrates", "Dietary Fiber",
                "Protein", "Vitamin A", "Vitamin C", 
                "Calcium", "Iron", "Calories", "Cholesterol", "Total Fat",
                "Sodium", "Carbohydrates", "Dietary Fiber",
                "Protein", "Vitamin A", "Vitamin C", 
                "Calcium", "Iron", "objective"]
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df)

def generate_slack_variables(index):
    slack_variables = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

    return np.array(matrix_coefficients)


def generate_objective_matrix(foods):
    objective_coefficients = []
    for food in foods:
        objective_coefficients.append(food_cost[food])
    objective_coefficients.extend(generate_slack_variables(22))
    objective_coefficients.extend([0])
    return np.array(objective_coefficients)



selected_foods = ["Frozen Broccoli", "Carrots Raw", "Celery Raw", "Frozen Corn", "Lettuce, Iceberg, Raw", 
                  "Roasted Chicken", "Potatoes, Baked", "Tofu", "Peppers, Sweet, Raw", "Spaghetti W/ Sauce", 
                  "Tomato, Red, Ripe, Raw", "Apple, Raw, W/ Skin", "Banana", "Grapes", "Kiwifruit, Raw, Fresh", 
                  "Oranges", "Bagels", "Wheat Bread", "White Bread", "Oatmeal Cookies"]


constraints_matrix = generate_constraints_matrix(selected_foods)
objective_matrix = generate_objective_matrix(selected_foods)
extended_matrix = np.vstack((constraints_matrix, objective_matrix))

variables = get_variables(selected_foods)
format_matrix(extended_matrix, variables)
simplex_matrix = sm.simplex_method(extended_matrix)
format_matrix(simplex_matrix, variables)
print(sm.get_solution(simplex_matrix))
#format(sm.simplex_method(generate_constraints_matrix(selected_foods)), variables)
